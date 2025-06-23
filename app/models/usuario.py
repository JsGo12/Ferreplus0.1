from sqlalchemy import Column, Integer, String, Enum
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    direccion = Column(String(200))
    telefono = Column(String(20))
    rol = Column(Enum("admin", "cliente"), default="cliente", nullable=False)
