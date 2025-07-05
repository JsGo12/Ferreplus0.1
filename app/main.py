import os
import sys

from dotenv import load_dotenv

# Cargar desde .env
load_dotenv()

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse

from app.routes import despachos
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import productos, auth, webpay, contacto, compras, estado_compras


app = FastAPI(
    title="FERREPLUS API",
    description="API REST para gestión de productos, usuarios, compras y pagos con Webpay",
    version="2.0.0"
)


# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# Proteccion
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ruta archivos estaticos y templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


# Rutas principales para servir HTML
@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/perfil", response_class=HTMLResponse)
def perfil_page(request: Request):
    return templates.TemplateResponse("perfil.html", {"request": request})

@app.get("/registro", response_class=HTMLResponse)
def registro_page(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.get("/gestion", response_class=HTMLResponse)
def gestion_page(request: Request):
    return templates.TemplateResponse("gestion.html", {"request": request})

@app.get("/finalizarc", response_class=HTMLResponse)
def finalizarc_page(request: Request):
    return templates.TemplateResponse("finalizarc.html", {"request": request})

@app.get("/contra", response_class=HTMLResponse)
def contra_page(request: Request):
    return templates.TemplateResponse("contra.html", {"request": request})

@app.get("/pago_ex", response_class=HTMLResponse)
def pago_ex_page(request: Request):
    return templates.TemplateResponse("pago_ex.html", {"request": request})    


# Incluir las rutas de la API (DEBEN IR ANTES DE LA RUTA CATCH-ALL)
app.include_router(productos.router)
app.include_router(auth.router)
app.include_router(webpay.router)
app.include_router(contacto.router)
app.include_router(compras.router)
app.include_router(estado_compras.router)
app.include_router(despachos.router)


print("✅ Rutas de Webpay cargadas")


# Ruta catch-all para 404 (DEBE IR AL FINAL)
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, full_path: str):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
