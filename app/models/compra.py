from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
        
    fecha = Column(DateTime, default=datetime.now)
    estado = Column(String(20), default="pendiente")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="compras")

    detalles = relationship("DetalleCompra", back_populates="compra")
    despacho = relationship("Despacho", back_populates="compra", uselist=False) 

    total = Column(Float, nullable=False, default=0.0)

    pago = relationship("Pago", back_populates="compra", uselist=False)
    
    detalles = relationship("DetalleCompra", back_populates="compra")

    

