from sqlalchemy.orm import Session
# Importar todos los modelos para que SQLAlchemy los registre antes de cualquier acceso
from app.models import usuario, compra, pago, producto, detalle_compra, despacho
# Importar todos los modelos para que SQLAlchemy los registre antes de cualquier acceso
from app.models.usuario import Usuario


from app.database import SessionLocal
from app.models.usuario import Usuario
from app.utils import hash_password

def crear_admin():
    db: Session = SessionLocal()

    correo_admin = "admin@ferremas.cl"
    usuario_existente = db.query(Usuario).filter(Usuario.correo == correo_admin).first()

    if usuario_existente:
        print("⚠️ El usuario administrador ya existe.")
        return

    nuevo_admin = Usuario(
        nombre="Administrador",
        correo=correo_admin,
        contraseña=hash_password("admin123"),
        direccion="Dirección Admin",
        telefono="123456789",
        rol="admin"
    )

    db.add(nuevo_admin)
    db.commit()
    db.refresh(nuevo_admin)

    print("✅ Usuario administrador creado correctamente.")

if __name__ == "__main__":
    crear_admin()
