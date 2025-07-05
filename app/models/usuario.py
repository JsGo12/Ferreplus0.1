from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    direccion = Column(String(200))
    telefono = Column(String(20))
    rol = Column(String(20), nullable=False, default="cliente")
    compras = relationship("Compra", back_populates="usuario", cascade="all, delete-orphan")
    pagos = relationship("Pago", back_populates="usuario", cascade="all, delete-orphan")
