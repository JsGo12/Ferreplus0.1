from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.database import get_db
from app.dependencies import only_admin

router = APIRouter()

@router.get("/productos", summary="Listar productos")
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

@router.post("/productos", summary="Crear producto")
def crear_producto(
    codigo: str,
    marca: str,
    nombre: str,
    categoria: str,
    stock: int,
    precio: float,
    db: Session = Depends(get_db),
    user=Depends(only_admin)
):
    existe = db.query(Producto).filter(Producto.codigo == codigo).first()
    if existe:
        raise HTTPException(status_code=400, detail="Ya existe un producto con ese código")
    nuevo = Producto(
        codigo=codigo,
        marca=marca,
        nombre=nombre,
        categoria=categoria,
        stock=stock,
        precio=precio
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/productos/{codigo}", summary="Eliminar producto")
def eliminar_producto(codigo: str, db: Session = Depends(get_db), user=Depends(only_admin)):
    producto = db.query(Producto).filter(Producto.codigo == codigo).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"detail": "Producto eliminado"}
