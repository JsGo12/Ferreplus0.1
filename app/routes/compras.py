from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.compra import Compra
from app.models.detalle_compra import DetalleCompra
from app.models.producto import Producto
from app.dependencies import get_current_user, only_admin
from datetime import datetime

router = APIRouter()

# Crear una nueva compra
@router.post("/compras")
def crear_compra(
    items: list[dict],  # [{codigo: str, cantidad: int}]
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if not items:
        raise HTTPException(status_code=400, detail="No se recibieron productos")

    total = 0
    detalle_items = []

    for item in items:
        producto = db.query(Producto).filter(Producto.codigo == item["codigo"]).first()
        if not producto or producto.stock < item["cantidad"]:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para {item['codigo']}")
        
        total += producto.precio * item["cantidad"]
        detalle_items.append((producto, item["cantidad"], producto.precio))

    nueva_compra = Compra(
        total=total,
        estado="pendiente",
        usuario_id=user["id"],
        fecha=datetime.now()
    )
    db.add(nueva_compra)
    db.commit()
    db.refresh(nueva_compra)

    for p, cantidad, precio_unitario in detalle_items:
        detalle = DetalleCompra(
            compra_id=nueva_compra.id,
            producto_codigo=p.codigo,
            cantidad=cantidad,
            precio_unitario=precio_unitario
        )
        db.add(detalle)
        p.stock -= cantidad  # descontar stock
    db.commit()

    return {"mensaje": "Compra realizada correctamente", "compra_id": nueva_compra.id, "total": total}

# Obtener compras (admin ve todas, usuario solo las suyas)
@router.get("/compras")
def listar_compras(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user["rol"] == "admin":
        return db.query(Compra).all()
    return db.query(Compra).filter(Compra.usuario_id == user["id"]).all()
