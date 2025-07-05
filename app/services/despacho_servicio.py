from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.despacho import Despacho
from app.models.compra import Compra
from typing import List, Optional
from fastapi import HTTPException
from app.repositorios.despacho_repo import DespachoCreate, DespachoUpdate

class DespachoService:
    
    @staticmethod
    def crear_despacho(db: Session, despacho_data: DespachoCreate) -> Despacho:
        """
        Crea un nuevo despacho
        """
        try:
            # Verificar que la compra existe
            compra = db.query(Compra).filter(Compra.id == despacho_data.compra_id).first()
            if not compra:
                raise HTTPException(status_code=404, detail="Compra no encontrada")
            
            # Verificar que la compra no tenga ya un despacho
            despacho_existente = db.query(Despacho).filter(Despacho.compra_id == despacho_data.compra_id).first()
            if despacho_existente:
                raise HTTPException(status_code=400, detail="La compra ya tiene un despacho asignado")
            
            # Crear el despacho
            nuevo_despacho = Despacho(**despacho_data.dict())
            db.add(nuevo_despacho)
            db.commit()
            db.refresh(nuevo_despacho)
            
            return nuevo_despacho
            
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Error de integridad en la base de datos")
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

    @staticmethod
    def obtener_despacho_por_id(db: Session, despacho_id: int) -> Optional[Despacho]:
        """
        Obtiene un despacho por su ID
        """
        return db.query(Despacho).filter(Despacho.id == despacho_id).first()

    @staticmethod
    def obtener_despacho_por_compra(db: Session, compra_id: int) -> Optional[Despacho]:
        """
        Obtiene un despacho por el ID de la compra
        """
        return db.query(Despacho).filter(Despacho.compra_id == compra_id).first()

    @staticmethod
    def obtener_todos_despachos(db: Session, skip: int = 0, limit: int = 100) -> List[Despacho]:
        """
        Obtiene todos los despachos con paginación
        """
        return db.query(Despacho).offset(skip).limit(limit).all()

    @staticmethod
    def obtener_despachos_por_estado(db: Session, estado: str, skip: int = 0, limit: int = 100) -> List[Despacho]:
        """
        Obtiene despachos filtrados por estado
        """
        return db.query(Despacho).filter(Despacho.estado_despacho == estado).offset(skip).limit(limit).all()

    @staticmethod
    def obtener_despachos_por_tipo(db: Session, tipo: str, skip: int = 0, limit: int = 100) -> List[Despacho]:
        """
        Obtiene despachos filtrados por tipo de entrega
        """
        return db.query(Despacho).filter(Despacho.tipo_entrega == tipo).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_despacho(db: Session, despacho_id: int, despacho_data: DespachoUpdate) -> Optional[Despacho]:
        """
        Actualiza un despacho existente
        """
        try:
            despacho = db.query(Despacho).filter(Despacho.id == despacho_id).first()
            if not despacho:
                return None

            # Actualizar solo los campos que no son None
            update_data = despacho_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(despacho, field, value)

            db.commit()
            db.refresh(despacho)
            return despacho
            
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar despacho: {str(e)}")

    @staticmethod
    def actualizar_estado_despacho(db: Session, despacho_id: int, nuevo_estado: str) -> Optional[Despacho]:
        """
        Actualiza solo el estado del despacho
        """
        estados_validos = ['pendiente', 'preparando', 'enviado', 'entregado']
        if nuevo_estado not in estados_validos:
            raise HTTPException(status_code=400, detail=f"Estado inválido. Estados válidos: {estados_validos}")

        try:
            despacho = db.query(Despacho).filter(Despacho.id == despacho_id).first()
            if not despacho:
                return None

            despacho.estado_despacho = nuevo_estado
            db.commit()
            db.refresh(despacho)
            return despacho
            
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar estado: {str(e)}")

    @staticmethod
    def eliminar_despacho(db: Session, despacho_id: int) -> bool:
        """
        Elimina un despacho (soft delete recomendado en producción)
        """
        try:
            despacho = db.query(Despacho).filter(Despacho.id == despacho_id).first()
            if not despacho:
                return False

            db.delete(despacho)
            db.commit()
            return True
            
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar despacho: {str(e)}")

    @staticmethod
    def obtener_estadisticas_despachos(db: Session) -> dict:
        """
        Obtiene estadísticas de los despachos
        """
        try:
            total_despachos = db.query(Despacho).count()
            
            # Contar por estado
            pendientes = db.query(Despacho).filter(Despacho.estado_despacho == 'pendiente').count()
            preparando = db.query(Despacho).filter(Despacho.estado_despacho == 'preparando').count()
            enviados = db.query(Despacho).filter(Despacho.estado_despacho == 'enviado').count()
            entregados = db.query(Despacho).filter(Despacho.estado_despacho == 'entregado').count()
            
            # Contar por tipo
            despachos_domicilio = db.query(Despacho).filter(Despacho.tipo_entrega == 'despacho').count()
            retiros = db.query(Despacho).filter(Despacho.tipo_entrega == 'retiro').count()
            
            return {
                "total_despachos": total_despachos,
                "por_estado": {
                    "pendientes": pendientes,
                    "preparando": preparando,
                    "enviados": enviados,
                    "entregados": entregados
                },
                "por_tipo": {
                    "despachos_domicilio": despachos_domicilio,
                    "retiros": retiros
                }
            }
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener estadísticas: {str(e)}")