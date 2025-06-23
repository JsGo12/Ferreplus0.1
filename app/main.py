import os
#import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.database import Base, engine
from app.routes import productos, auth, webpay, contacto, compras, estado_compras

# ✅ Cargar variables desde .env (COMMERCE_CODE, API_KEY, RETURN_URL)
load_dotenv()

app = FastAPI(
    title="FERREPLUS API",
    description="API REST para gestión de productos, usuarios, compras y pagos con Webpay",
    version="2.0.0"
)

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a FERREPLUS. Usa /docs para ver la API"}

# Incluir las rutas
app.include_router(productos.router)
app.include_router(auth.router)
app.include_router(webpay.router)
app.include_router(contacto.router)
app.include_router(compras.router)
app.include_router(estado_compras.router)
