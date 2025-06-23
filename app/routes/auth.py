from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.database import get_db
from app.services.auth import verify_password, hash_password, create_access_token

router = APIRouter()

@router.post("/login", summary="Iniciar sesión y obtener token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.correo == form_data.username).first()
    if not user or not verify_password(form_data.password, user.contraseña):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    
    token = create_access_token(data={"sub": user.correo, "rol": user.rol, "id": user.id})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", summary="Registrar nuevo usuario")
def register(nombre: str, correo: str, password: str, rol: str = "cliente", db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    nuevo = Usuario(
        nombre=nombre,
        correo=correo,
        contraseña=hash_password(password),
        rol=rol
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"detail": "Usuario creado correctamente"}
