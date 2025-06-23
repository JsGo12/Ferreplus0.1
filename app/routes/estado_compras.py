from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.compra import Compra
from app.dependencies import only_admin
from pydantic import BaseModel

router = APIRouter()

class EstadoUpdate(BaseModel):
    estado: str

@router.put("/compras/{id}/estado")
def actualizar_estado_compra(
    id: int,
    estado: EstadoUpdate,
    db: Session = Depends(get_db),
    user=Depends(only_admin)
):
    compra = db.query(Compra).filter(Compra.id == id).first()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    
    compra.estado = estado.estado
    db.commit()
    return {"mensaje": f"Compra {id} actualizada a estado: {estado.estado}"}
