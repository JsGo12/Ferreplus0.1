import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import APIRouter, Form, Depends
from fastapi.responses import HTMLResponse
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType
from transbank.error.transbank_error import TransbankError
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pago import Pago

# Variables estáticas
COMMERCE_CODE = os.getenv("COMMERCE_CODE")
API_KEY = os.getenv("API_KEY")

RETURN_URL = os.getenv("RETURN_URL")
print("🧪 RETURN_URL en tiempo real:", RETURN_URL)  # ✅ Confirmación visual

router = APIRouter()

@router.get("/webpay", response_class=HTMLResponse)
async def index():
    return '''
        <h2>Pagar con Webpay Plus</h2>
        <form action="/webpay/pagar" method="post">
            <input type="submit" value="Pagar $1.000">
        </form>
    '''

@router.post("/webpay/pagar", response_class=HTMLResponse)
async def pagar():
    try:

        options = WebpayOptions(
            commerce_code=COMMERCE_CODE,
            api_key=API_KEY,
            integration_type=IntegrationType.TEST
        )

        tx = Transaction(options)
        response = tx.create(
            buy_order="orden1234",
            session_id="sesion1234",
            amount=1000,
            return_url=RETURN_URL
        )

        token = response['token']
        url = response['url']

        return f"""
            <form id="webpay-form" action="{url}" method="POST">
                <input type="hidden" name="token_ws" value="{token}" />
            </form>
            <script>document.getElementById('webpay-form').submit();</script>
        """

    except TransbankError as e:
        return f"<h2>ERROR al crear transacción:</h2><pre>{str(e)}</pre>"
    except Exception as e:
        return f"<h2>ERROR inesperado:</h2><pre>{str(e)}</pre>"

@router.post("/webpay/retorno", response_class=HTMLResponse)
async def retorno(token_ws: str = Form(...), db: Session = Depends(get_db)):
    try:
        options = WebpayOptions(
            commerce_code=COMMERCE_CODE,
            api_key=API_KEY,
            integration_type=IntegrationType.TEST
        )
        tx = Transaction(options)
        result = tx.commit(token_ws)

        pago = db.query(Pago).filter(Pago.token == token_ws).first()
        if pago:
            pago.estado = result["status"]
            db.commit()

        return f"""
            <h3>Resultado de la transacción</h3>
            <ul>
                <li>Estado: {result["status"]}</li>
                <li>Monto: {result["amount"]}</li>
                <li>Orden: {result["buy_order"]}</li>
                <li>Código de autorización: {result["authorization_code"]}</li>
            </ul>
            <a href="/">Volver</a>
        """
    except Exception as e:
        return f"<h2>Error al confirmar el pago:</h2><pre>{str(e)}</pre>"
