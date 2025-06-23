from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, nullable=False)
    marca = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50))
    stock = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)
