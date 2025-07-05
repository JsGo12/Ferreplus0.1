from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Text
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class Despacho(Base):
    __tablename__ = "despachos"

    id = Column(Integer, primary_key=True, index=True)
    fecha_creacion = Column(DateTime, default=datetime.now)
    # Campos basados en el formulario JavaScript
    tipo_entrega = Column(String(20), nullable=False)  # 'despacho' o 'retiro'
    direccion = Column(Text, nullable=True)  # Solo requerido si tipo_entrega es 'despacho'
    rut = Column(String(12), nullable=False)  # RUT del receptor
    # Campos adicionales útiles para el despacho
    nombre_completo = Column(String(100), nullable=True)
    telefono_receptor = Column(String(15), nullable=True)  
    # Estado del despacho
    estado_despacho = Column(String(20), default="pendiente")  # pendiente, preparando, enviado, entregado
    compra_id = Column(Integer, ForeignKey("compras.id"), nullable=False, unique=True)
    compra = relationship("Compra", back_populates="despacho")


