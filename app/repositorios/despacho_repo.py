from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator
import re




# ==================== ESQUEMAS PYDANTIC ====================

class DespachoBase(BaseModel):
    tipo_entrega: str
    direccion: Optional[str] = None
    rut: str
    nombre_completo: Optional[str] = None
    telefono_receptor: Optional[str] = None

    @validator('tipo_entrega')
    def validar_tipo_entrega(cls, v):
        if v not in ['despacho', 'retiro']:
            raise ValueError('tipo_entrega debe ser "despacho" o "retiro"')
        return v

    @validator('direccion')
    def validar_direccion(cls, v, values):
        if values.get('tipo_entrega') == 'despacho' and not v:
            raise ValueError('La dirección es requerida para tipo_entrega "despacho"')
        return v

    @validator('rut')
    def validar_rut(cls, v):
        if not v:
            raise ValueError('El RUT es requerido')
        # Eliminar puntos y guiones
        rut_limpio = re.sub(r'[.-]', '', v)
        if len(rut_limpio) < 8 or len(rut_limpio) > 9:
            raise ValueError('El RUT debe tener entre 8 y 9 caracteres')
        return v

    @validator('telefono_receptor')
    def validar_telefono(cls, v):
        if v and not re.match(r'^\+?[\d\s-]{8,15}$', v):
            raise ValueError('Formato de teléfono inválido')
        return v

class DespachoCreate(DespachoBase):
    compra_id: int

class DespachoUpdate(BaseModel):
    tipo_entrega: Optional[str] = None
    direccion: Optional[str] = None
    rut: Optional[str] = None
    nombre_completo: Optional[str] = None
    telefono_receptor: Optional[str] = None
    estado_despacho: Optional[str] = None

    @validator('tipo_entrega')
    def validar_tipo_entrega(cls, v):
        if v and v not in ['despacho', 'retiro']:
            raise ValueError('tipo_entrega debe ser "despacho" o "retiro"')
        return v

    @validator('estado_despacho')
    def validar_estado_despacho(cls, v):
        if v and v not in ['pendiente', 'preparando', 'enviado', 'entregado']:
            raise ValueError('estado_despacho debe ser uno de: pendiente, preparando, enviado, entregado')
        return v

class DespachoResponse(DespachoBase):
    id: int
    fecha_creacion: datetime
    estado_despacho: str
    compra_id: int

    class Config:
        from_attributes = True

class DespachoWithCompra(DespachoResponse):
    compra: dict

    class Config:
        from_attributes = True
