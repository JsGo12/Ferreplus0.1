from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from sqlalchemy.orm import relationship


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, nullable=False)
    marca = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=True)
    stock = Column(Integer, nullable=False, default=0)
    precio = Column(Float, nullable=False, default=0.0)
    imagen = Column(String(500), nullable=True)  # URL o base64 si lo deseas

    detalles = relationship("DetalleCompra", back_populates="producto")

