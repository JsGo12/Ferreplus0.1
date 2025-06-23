from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)
    moneda = Column(String(10), default="CLP")
    fecha_creacion = Column(DateTime, default=datetime.now)
    fecha_actualizacion = Column(DateTime)
    token = Column(String(200))
    url_redireccion = Column(String(300))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    compra_id = Column(Integer, ForeignKey("compras.id"))
