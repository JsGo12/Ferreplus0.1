from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.database import get_db
from app.dependencies import only_admin
import shutil
import os
from uuid import uuid4
import logging

# Configurar logging para ver errores detallados
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/productos", summary="Listar productos")
def listar_productos(db: Session = Depends(get_db)):
    try:
        productos = db.query(Producto).all()
        logger.info(f"Productos obtenidos: {len(productos)}")
        return productos
    except Exception as e:
        logger.error(f"Error al listar productos: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error interno del servidor al listar productos: {str(e)}")


@router.post("/productos", summary="Crear producto con imagen")
async def crear_producto(
    codigo: str = Form(...),
    marca: str = Form(...),
    nombre: str = Form(...),
    categoria: str = Form(...),
    descripcion: str = Form(...),
    stock: int = Form(...),
    precio: float = Form(...),
    imagen: UploadFile = File(None),
    db: Session = Depends(get_db),
    user=Depends(only_admin)
):
    # Verificar si ya existe
    existe = db.query(Producto).filter(Producto.codigo == codigo).first()
    if existe:
        raise HTTPException(status_code=400, detail="Ya existe un producto con ese código")

    ruta_imagen = None
    if imagen and imagen.filename:
        # Obtener la extensión del archivo
        ext = os.path.splitext(imagen.filename)[1]
        if not ext:
            ext = '.jpg'  # Extensión por defecto si no se detecta
            
        # Generar nombre único para el archivo
        nombre_archivo = f"{uuid4().hex}{ext}"
        ruta_carpeta = "app/static/imagenes"
        
        # Crear carpeta si no existe
        os.makedirs(ruta_carpeta, exist_ok=True)
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

        # Guardar el archivo
        try:
            with open(ruta_completa, "wb") as f:
                contenido = await imagen.read()
                f.write(contenido)
            
            # Usar el nombre real del archivo generado
            ruta_imagen = f"/static/imagenes/{nombre_archivo}"
        except Exception as e:
            logger.error(f"Error al guardar la imagen: {str(e)}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"Error al guardar la imagen: {str(e)}")

    nuevo = Producto(
        codigo=codigo,
        marca=marca,
        nombre=nombre,
        categoria=categoria,
        descripcion=descripcion,
        stock=stock,
        precio=precio,
        imagen=ruta_imagen
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"detail": "Producto creado correctamente", "producto": {
        "id": nuevo.id,
        "codigo": nuevo.codigo,
        "nombre": nuevo.nombre,
        "imagen": nuevo.imagen
    }}


@router.put("/productos/{codigo}", summary="Actualizar producto")
async def actualizar_producto(
    codigo: str,
    marca: str = Form(...),
    nombre: str = Form(...),
    categoria: str = Form(...),
    descripcion: str = Form(...),
    stock: int = Form(...),
    precio: float = Form(...),
    imagen: UploadFile = File(None),
    db: Session = Depends(get_db),
    user=Depends(only_admin)
):
    # Buscar el producto existente
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Actualizar campos básicos
    producto.marca = marca
    producto.nombre = nombre
    producto.categoria = categoria
    producto.descripcion = descripcion
    producto.stock = stock
    producto.precio = precio

    # Si se proporciona una nueva imagen
    if imagen and imagen.filename:
        # Eliminar imagen anterior si existe
        if producto.imagen:
            ruta_anterior = f"app{producto.imagen}"
            if os.path.exists(ruta_anterior):
                try:
                    os.remove(ruta_anterior)
                except Exception as e:
                    logger.warning(f"No se pudo eliminar la imagen anterior {ruta_anterior}: {str(e)}")
                    pass  # Si no se puede eliminar, continúa

        # Guardar nueva imagen
        ext = os.path.splitext(imagen.filename)[1]
        if not ext:
            ext = '.jpg'
            
        nombre_archivo = f"{uuid4().hex}{ext}"
        ruta_carpeta = "app/static/imagenes"
        os.makedirs(ruta_carpeta, exist_ok=True)
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

        try:
            with open(ruta_completa, "wb") as f:
                contenido = await imagen.read()
                f.write(contenido)
            
            producto.imagen = f"/static/imagenes/{nombre_archivo}"
        except Exception as e:
            logger.error(f"Error al guardar la nueva imagen: {str(e)}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"Error al guardar la nueva imagen: {str(e)}")

    db.commit()
    db.refresh(producto)
    return {"detail": "Producto actualizado correctamente"}


@router.delete("/productos/{codigo}", summary="Eliminar producto")
def eliminar_producto(codigo: str, db: Session = Depends(get_db), user=Depends(only_admin)):
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Eliminar imagen si existe
    if producto.imagen:
        ruta_imagen = f"app{producto.imagen}"
        if os.path.exists(ruta_imagen):
            try:
                os.remove(ruta_imagen)
            except Exception as e:
                logger.warning(f"No se pudo eliminar la imagen del producto {ruta_imagen}: {str(e)}")
                pass  # Si no se puede eliminar, continúa
    
    db.delete(producto)
    db.commit()
    return {"detail": "Producto eliminado"}
