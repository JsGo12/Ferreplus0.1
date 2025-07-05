from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.contacto import Contacto

router = APIRouter()

@router.post("/contacto")
def enviar_contacto(
    nombre: str,
    email: str,
    asunto: str,
    mensaje: str,
    db: Session = Depends(get_db)
):
    nuevo = Contacto(
        nombre=nombre,
        email=email,
        asunto=asunto,
        mensaje=mensaje
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"detalle": "Mensaje recibido correctamente"}
