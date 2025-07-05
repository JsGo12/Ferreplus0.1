from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.services.despacho_servicio import DespachoService
import re
from app.repositorios.despacho_repo import DespachoCreate, DespachoUpdate,DespachoResponse



# ==================== RUTAS/ENDPOINTS ====================

router = APIRouter(
    prefix="/despachos",
    tags=["despachos"],
    responses={404: {"description": "No encontrado"}}
)

@router.post("/", response_model=DespachoResponse, status_code=201)
def crear_despacho(
    despacho: DespachoCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un nuevo despacho para una compra
    """
    return DespachoService.crear_despacho(db, despacho)

@router.get("/", response_model=List[DespachoResponse])
def obtener_despachos(
    skip: int = Query(0, ge=0, description="Número de registros a omitir"),
    limit: int = Query(100, ge=1, le=100, description="Número máximo de registros a devolver"),
    estado: Optional[str] = Query(None, description="Filtrar por estado del despacho"),
    tipo: Optional[str] = Query(None, description="Filtrar por tipo de entrega"),
    db: Session = Depends(get_db)
):
    """
    Obtiene una lista de despachos con filtros opcionales
    """
    if estado and tipo:
        # Si se proporcionan ambos filtros, aplicar ambos
        despachos = db.query(DespachoService.Despacho).filter(
            DespachoService.Despacho.estado_despacho == estado,
            DespachoService.Despacho.tipo_entrega == tipo
        ).offset(skip).limit(limit).all()
    elif estado:
        despachos = DespachoService.obtener_despachos_por_estado(db, estado, skip, limit)
    elif tipo:
        despachos = DespachoService.obtener_despachos_por_tipo(db, tipo, skip, limit)
    else:
        despachos = DespachoService.obtener_todos_despachos(db, skip, limit)
    
    return despachos

@router.get("/{despacho_id}", response_model=DespachoResponse)
def obtener_despacho(
    despacho_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene un despacho por su ID
    """
    despacho = DespachoService.obtener_despacho_por_id(db, despacho_id)
    if not despacho:
        raise HTTPException(status_code=404, detail="Despacho no encontrado")
    return despacho

@router.get("/compra/{compra_id}", response_model=DespachoResponse)
def obtener_despacho_por_compra(
    compra_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene el despacho asociado a una compra específica
    """
    despacho = DespachoService.obtener_despacho_por_compra(db, compra_id)
    if not despacho:
        raise HTTPException(status_code=404, detail="No se encontró despacho para esta compra")
    return despacho

@router.put("/{despacho_id}", response_model=DespachoResponse)
def actualizar_despacho(
    despacho_id: int,
    despacho_data: DespachoUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza un despacho existente
    """
    despacho = DespachoService.actualizar_despacho(db, despacho_id, despacho_data)
    if not despacho:
        raise HTTPException(status_code=404, detail="Despacho no encontrado")
    return despacho

@router.patch("/{despacho_id}/estado", response_model=DespachoResponse)
def actualizar_estado_despacho(
    despacho_id: int,
    nuevo_estado: str = Query(..., description="Nuevo estado del despacho"),
    db: Session = Depends(get_db)
):
    """
    Actualiza únicamente el estado de un despacho
    """
    despacho = DespachoService.actualizar_estado_despacho(db, despacho_id, nuevo_estado)
    if not despacho:
        raise HTTPException(status_code=404, detail="Despacho no encontrado")
    return despacho

@router.delete("/{despacho_id}", status_code=204)
def eliminar_despacho(
    despacho_id: int,
    db: Session = Depends(get_db)
):
    """
    Elimina un despacho
    """
    if not DespachoService.eliminar_despacho(db, despacho_id):
        raise HTTPException(status_code=404, detail="Despacho no encontrado")

@router.get("/estadisticas/resumen", response_model=dict)
def obtener_estadisticas_despachos(db: Session = Depends(get_db)):
    """
    Obtiene estadísticas generales de los despachos
    """
    return DespachoService.obtener_estadisticas_despachos(db)

# Endpoints adicionales útiles

@router.get("/pendientes/lista", response_model=List[DespachoResponse])
def obtener_despachos_pendientes(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Obtiene todos los despachos pendientes (helper endpoint)
    """
    return DespachoService.obtener_despachos_por_estado(db, "pendiente", skip, limit)

@router.post("/{despacho_id}/marcar-enviado", response_model=DespachoResponse)
def marcar_como_enviado(
    despacho_id: int,
    db: Session = Depends(get_db)
):
    """
    Marca un despacho como enviado (helper endpoint)
    """
    despacho = DespachoService.actualizar_estado_despacho(db, despacho_id, "enviado")
    if not despacho:
        raise HTTPException(status_code=404, detail="Despacho no encontrado")
    return despacho

@router.post("/{despacho_id}/marcar-entregado", response_model=DespachoResponse)
def marcar_como_entregado(
    despacho_id: int,
    db: Session = Depends(get_db)
):
    """
    Marca un despacho como entregado (helper endpoint)
    """
    despacho = DespachoService.actualizar_estado_despacho(db, despacho_id, "entregado")
    if not despacho:
        raise HTTPException(status_code=404, detail="Despacho no encontrado")
    return despacho