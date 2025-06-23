from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

options = WebpayOptions(
    commerce_code="597055555532",
    api_key="597055555532",  # Usa el mismo código como API Key
    integration_type=IntegrationType.TEST
)

tx = Transaction(options)

response = tx.create(
    buy_order="orden123abc",
    session_id="sesion123abc",
    amount=1000,
    return_url="https://webhook.site/20516b95-e0ed-455c-9d64-76ea5e68808d/webpay/retorno"
)

print("✅ Transacción creada:")
print(response)
