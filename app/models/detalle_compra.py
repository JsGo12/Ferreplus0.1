from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DetalleCompra(Base):
    __tablename__ = "detalle_compra"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))  # ✅ Esto es lo que falta
    compra_id = Column(Integer, ForeignKey("compras.id"))
    cantidad = Column(Integer)
    precio_unitario = Column(Float)

    # Relaciones (opcional si las necesitas)
    producto = relationship("Producto", back_populates="detalles")
    compra = relationship("Compra", back_populates="detalles")
