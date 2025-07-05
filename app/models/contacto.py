from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class Contacto(Base):
    __tablename__ = "contacto"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100))
    asunto = Column(String(200))
    mensaje = Column(Text)
    fecha = Column(DateTime, default=datetime.now)
