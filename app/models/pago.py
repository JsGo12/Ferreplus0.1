from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Text
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)
    moneda = Column(String(10), default="CLP")
    fecha_creacion = Column(DateTime, default=datetime.now)
    fecha_actualizacion = Column(DateTime)
    token = Column(String(200))
    url_redireccion = Column(String(300))
    estado = Column(String(50), default="PENDING")  # PENDING, AUTHORIZED, REJECTED, etc.
    buy_order = Column(String(100))  # Para almacenar la orden de compra
    authorization_code = Column(String(50))  # Código de autorización
    response_details = Column(Text)  # Para almacenar respuesta completa de Webpay
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="pagos")
    compra_id = Column(Integer, ForeignKey("compras.id"), nullable=False, unique=True)
    compra = relationship("Compra", back_populates="pago")