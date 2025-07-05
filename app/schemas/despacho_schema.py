# app/schemas/despacho_schema.py
from pydantic import BaseModel

class DespachoCreate(BaseModel):
    tipo_entrega: str
    direccion: str
    rut: str
    nombre_completo: str
    compra_id: int
