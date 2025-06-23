from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.now)
    estado = Column(String(20), default="pendiente")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario")
    detalles = relationship("DetalleCompra", back_populates="compra")
