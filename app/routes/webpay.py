import os
import logging
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from fastapi import APIRouter, Form, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType
from transbank.error.transbank_error import TransbankError

from app.database import get_db
from app.models.pago import Pago
from app.models.compra import Compra
from app.models.detalle_compra import DetalleCompra
from app.models.contacto import Contacto
from app.schemas.despacho_schema import DespachoCreate
from app.services.despacho_servicio import DespachoService
from app.dependencies import get_current_user
from app.models.producto import Producto

import json

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Variables de configuración
COMMERCE_CODE = os.getenv("COMMERCE_CODE", "597055555532")
API_KEY = os.getenv("API_KEY")
RETURN_URL = os.getenv("RETURN_URL")  # URL para que Webpay retorne a tu backend
WEB_RETURN_URL = os.getenv("WEB_PAY_URL_RETURN")  # URL para redirigir al frontend

# Validaciones
if not RETURN_URL:
    raise ValueError("RETURN_URL no está configurada en las variables de entorno")

if not WEB_RETURN_URL:
    raise ValueError("WEB_PAY_URL_RETURN no está configurada en las variables de entorno")

if not API_KEY:
    raise ValueError("API_KEY no está configurada en las variables de entorno")

webpay_options = WebpayOptions(
    commerce_code=COMMERCE_CODE,
    api_key=API_KEY,
    integration_type=IntegrationType.TEST
)

router = APIRouter()

@router.post("/webpay/iniciar", response_class=HTMLResponse)
async def iniciar_pago(
    nombre: str = Form(...),
    rut: str = Form(...),
    email: str = Form(...),
    envio: str = Form(...),
    direccion: str = Form(""),
    total: float = Form(...),
    carrito: str = Form(...),
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    try:
        logger.info(f"🚀 Iniciando pago de {total} CLP para usuario {user['id']}")

        # Validar y parsear carrito
        try:
            carrito_items = json.loads(carrito)
        except json.JSONDecodeError as e:
            logger.error(f"❌ Error al parsear carrito JSON: {e}")
            raise HTTPException(status_code=400, detail="Formato de carrito inválido")

        if not carrito_items:
            raise HTTPException(status_code=400, detail="Carrito vacío")

        # Crear compra
        compra = Compra(
            total=total,
            estado="pendiente",
            fecha=datetime.now(),
            usuario_id=user["id"]
        )
        db.add(compra)
        db.flush()  # Usar flush en lugar de commit para obtener el ID sin confirmar
        
        # Validar productos y stock antes de procesar
        productos_validados = []
        for item in carrito_items:
            producto_id = item.get('producto_id') or item.get('id')
            producto = None
            
            if producto_id:
                producto = db.query(Producto).filter(Producto.id == producto_id).first()
            elif item.get("codigo"):
                producto = db.query(Producto).filter(Producto.codigo == item["codigo"]).first()

            if not producto:
                nombre_error = item.get("nombre", item.get("codigo", "desconocido"))
                logger.error(f"❌ Producto no encontrado: {nombre_error}")
                raise HTTPException(status_code=400, detail=f"Producto no encontrado: {nombre_error}")

            cantidad_solicitada = item.get('cantidad', 0)
            if not isinstance(cantidad_solicitada, int) or cantidad_solicitada <= 0:
                raise HTTPException(status_code=400, detail=f"Cantidad inválida para producto: {producto.nombre}")

            logger.info(f"🔍 Producto: {producto.nombre} | Stock: {producto.stock} | Cantidad solicitada: {cantidad_solicitada}")

            if producto.stock < cantidad_solicitada:
                logger.error(f"❌ Stock insuficiente para: {producto.nombre}")
                raise HTTPException(status_code=400, detail=f"Stock insuficiente para: {producto.nombre}")

            productos_validados.append({
                'producto': producto,
                'cantidad': cantidad_solicitada,
                'precio_unitario': item.get('precio_unitario') or item.get('precio', 0)
            })

        # Guardar detalles y actualizar stock
        for item_validado in productos_validados:
            producto = item_validado['producto']
            cantidad = item_validado['cantidad']
            precio_unitario = item_validado['precio_unitario']

            detalle = DetalleCompra(
                producto_id=producto.id,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                compra_id=compra.id
            )
            producto.stock -= cantidad
            db.add(detalle)

        # Registrar contacto
        contacto = Contacto(
            nombre=nombre,
            email=email,
            mensaje=f"Compra generada con RUT {rut}",
            fecha=datetime.now()
        )
        db.add(contacto)

        # Crear despacho si aplica
        if envio == "despacho" and direccion.strip():
            try:
                despacho_data = DespachoCreate(
                    tipo_entrega="despacho",
                    direccion=direccion,
                    rut=rut,
                    nombre_completo=nombre,
                    compra_id=compra.id
                )
                DespachoService.crear_despacho(db, despacho_data)
            except Exception as despacho_error:
                logger.error(f"❌ Error al crear despacho: {despacho_error}")
                # No fallar todo el proceso por error de despacho
                pass

        # Generar datos Webpay
        buy_order = f"ferreplus_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        try:
            tx = Transaction(webpay_options)
            response = tx.create(
                buy_order=buy_order,
                session_id=session_id,
                amount=int(total),  # Asegurar que sea entero
                return_url=RETURN_URL
            )

            token = response['token']
            url = response['url']

            pago = Pago(
                monto=total,
                moneda="CLP",
                fecha_creacion=datetime.now(),
                token=token,
                url_redireccion=url,
                compra_id=compra.id,
                usuario_id=user["id"]
            )
            db.add(pago)
            db.commit()  # Confirmar todo si llegamos hasta aquí

            logger.info(f"✅ Pago creado exitosamente. Token: {token}")

            return f"""
            <html>
            <body>
                <form id='webpay-form' action='{url}' method='POST'>
                    <input type='hidden' name='token_ws' value='{token}' />
                </form>
                <script>document.getElementById('webpay-form').submit();</script>
            </body>
            </html>
            """

        except TransbankError as tb_error:
            logger.error(f"❌ Error de Transbank: {tb_error}")
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error en Transbank: {str(tb_error)}")

    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        logger.error(f"❌ Error inesperado en iniciar_pago: {e}", exc_info=True)
        db.rollback()
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.post("/webpay/retorno", response_class=HTMLResponse)
@router.get("/webpay/retorno", response_class=HTMLResponse)
async def retorno(request: Request, token_ws: str = None, db: Session = Depends(get_db)):
    try:
        # Obtener token desde formulario o query params
        if not token_ws:
            if request.method == "POST":
                form_data = await request.form()
                token_ws = form_data.get("token_ws")
            else:
                token_ws = request.query_params.get("token_ws")

        if not token_ws:
            logger.error("❌ Token no encontrado en la solicitud")
            return HTMLResponse(content=f"""
            <html>
            <head><title>Error de Pago</title></head>
            <body>
                <h1>❌ Error de Pago</h1>
                <p>No se pudo procesar la transacción. Redirigiendo...</p>
                <script>
                    setTimeout(function() {{
                        window.location.href = '{WEB_RETURN_URL}?status=error&message=' + encodeURIComponent('Token no encontrado');
                    }}, 3000);
                </script>
            </body>
            </html>
            """, status_code=400)

        logger.info(f"🔄 Procesando retorno de Webpay con token: {token_ws}")
        logger.info(f"📋 Método HTTP: {request.method}")

        # Buscar el pago en la base de datos
        pago = db.query(Pago).filter(Pago.token == token_ws).first()
        if not pago:
            logger.error(f"❌ Pago no encontrado para token: {token_ws}")
            return HTMLResponse(content=f"""
            <html>
            <head><title>Error de Pago</title></head>
            <body>
                <h1>❌ Pago no encontrado</h1>
                <p>La transacción no pudo ser localizada. Redirigiendo...</p>
                <script>
                    setTimeout(function() {{
                        window.location.href = '{WEB_RETURN_URL}?status=error&message=' + encodeURIComponent('Pago no encontrado');
                    }}, 3000);
                </script>
            </body>
            </html>
            """, status_code=404)

        try:
            # Confirmar transacción con Transbank
            tx = Transaction(webpay_options)
            result = tx.commit(token_ws)
            
            logger.info(f"✅ Respuesta de Transbank: {result}")

            # Verificar el estado de la transacción
            response_code = result.get("response_code")
            status_transbank = result.get("status", "").upper()
            
            # Actualizar campos comunes
            pago.fecha_actualizacion = datetime.now()
            pago.response_details = str(result)
            
            # Actualizar estado del pago según la respuesta
            if response_code == 0 and status_transbank == "AUTHORIZED":
                # Transacción exitosa
                pago.estado = "AUTHORIZED"
                pago.authorization_code = result.get("authorization_code")
                
                # Actualizar compra
                compra = db.query(Compra).filter(Compra.id == pago.compra_id).first()
                if compra:
                    compra.estado = "pagado"
                
                db.commit()
                
                logger.info(f"✅ Pago autorizado exitosamente. Orden: {pago.buy_order}")
                
                # Crear parámetros para la redirección
                params = {
                    'status': 'success',
                    'authorization_code': result.get("authorization_code", ""),
                    'amount': str(result.get("amount", pago.monto)),
                    'order_id': str(pago.buy_order),
                    'message': 'Pago autorizado exitosamente'
                }
                
                # Redirigir a página de éxito
                return HTMLResponse(content=f"""
                <html>
                <head><title>Pago Autorizado</title></head>
                <body>
                    <h1>✅ Pago Autorizado Exitosamente</h1>
                    <p>Redirigiendo...</p>
                    <script>
                        const params = new URLSearchParams({{
                            'status': 'success',
                            'authorization_code': '{result.get("authorization_code", "")}',
                            'amount': '{result.get("amount", pago.monto)}',
                            'order_id': '{pago.buy_order}',
                            'message': 'Pago autorizado exitosamente'
                        }});
                        window.location.href = '{WEB_RETURN_URL}?' + params.toString();
                    </script>
                </body>
                </html>
                """)
                
            elif response_code != 0 or status_transbank == "REJECTED":
                # Transacción rechazada
                pago.estado = "REJECTED"
                
                # Revertir stock y actualizar compra
                compra = db.query(Compra).filter(Compra.id == pago.compra_id).first()
                if compra:
                    compra.estado = "cancelado"
                    detalles = db.query(DetalleCompra).filter(DetalleCompra.compra_id == compra.id).all()
                    for detalle in detalles:
                        producto = db.query(Producto).filter(Producto.id == detalle.producto_id).first()
                        if producto:
                            producto.stock += detalle.cantidad
                
                db.commit()
                
                logger.warning(f"❌ Pago rechazado. Código de respuesta: {response_code}")
                
                return HTMLResponse(content=f"""
                <html>
                <head><title>Pago Rechazado</title></head>
                <body>
                    <h1>❌ Pago Rechazado</h1>
                    <p>Redirigiendo...</p>
                    <script>
                        const params = new URLSearchParams({{
                            'status': 'failed',
                            'response_code': '{response_code}',
                            'order_id': '{pago.buy_order}',
                            'message': 'Pago rechazado por el banco'
                        }});
                        window.location.href = '{WEB_RETURN_URL}?' + params.toString();
                    </script>
                </body>
                </html>
                """)
                
            else:
                # Estado desconocido - mantener como PENDING
                pago.estado = "PENDING"
                db.commit()
                
                logger.warning(f"⚠️ Estado de pago desconocido. Status: {status_transbank}, Code: {response_code}")
                
                return HTMLResponse(content=f"""
                <html>
                <head><title>Estado Desconocido</title></head>
                <body>
                    <h1>⚠️ Estado Desconocido</h1>
                    <p>Redirigiendo...</p>
                    <script>
                        const params = new URLSearchParams({{
                            'status': 'error',
                            'message': 'Estado de transacción desconocido: {status_transbank}',
                            'order_id': '{pago.buy_order}'
                        }});
                        window.location.href = '{WEB_RETURN_URL}?' + params.toString();
                    </script>
                </body>
                </html>
                """)

        except TransbankError as tb_error:
            logger.error(f"❌ Error de Transbank en retorno: {tb_error}")
            pago.estado = "REJECTED"
            pago.fecha_actualizacion = datetime.now()
            pago.response_details = str(tb_error)
            db.commit()
            
            return HTMLResponse(content=f"""
            <html>
            <head><title>Error de Transbank</title></head>
            <body>
                <h1>❌ Error de Transbank</h1>
                <p>Redirigiendo...</p>
                <script>
                    const params = new URLSearchParams({{
                        'status': 'error',
                        'message': 'Error en el procesamiento del pago',
                        'error_detail': '{str(tb_error)}',
                        'order_id': '{pago.buy_order}'
                    }});
                    window.location.href = '{WEB_RETURN_URL}?' + params.toString();
                </script>
            </body>
            </html>
            """, status_code=500)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error inesperado en retorno: {e}", exc_info=True)
        return HTMLResponse(content=f"""
        <html>
        <head><title>Error Inesperado</title></head>
        <body>
            <h1>❌ Error Inesperado</h1>
            <p>Redirigiendo...</p>
            <script>
                const params = new URLSearchParams({{'status': 'error', 'message': 'Error interno del servidor'}});
                window.location.href = '{WEB_RETURN_URL}?' + params.toString();
            </script>
        </body>
        </html>
        """, status_code=500)
    
@router.get("/webpay/debug")
def debug_webpay():
    return {
        "message": "Ruta de Webpay activa",
        "commerce_code": COMMERCE_CODE,
        "api_key_configured": bool(API_KEY),
        "return_url": RETURN_URL,
        "web_return_url": WEB_RETURN_URL,
        "integration_type": "TEST"
    }