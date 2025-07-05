# 🛠️ Proyecto Final FERREPLUS — ASY5131 (Duoc UC)

## 📘 Contexto del Proyecto

FERREPLUS es una plataforma de comercio electrónico desarrollada para "FERREMAS", una distribuidora de productos de ferretería y construcción con presencia nacional.  
Debido a la pandemia y la baja en ventas físicas, FERREMAS decidió implementar un sistema de ventas online para mejorar su eficiencia operativa y experiencia de usuario.

---

## 🧩 ¿Qué hace el sistema?

- Catálogo de productos con stock en tiempo real
- Carrito de compras con integración WebPay (Sandbox)
- Registro y login de clientes
- Login para administradores, vendedores, bodegueros y contadores
- Módulo de despacho a domicilio o retiro en tienda
- Registro de contacto y seguimiento
- API REST para productos (consumo interno y externo)

---

## ⚙️ Paso a paso para ejecutar el sistema

### 🔧 Requisitos:

- Python 3.10+
- XAMPP (para importar la base de datos ferremas_plus.sql usando phpMyAdmin)
- MySQL 8.0+ (incluido en XAMPP)
- Ngrok (ya incluido en el repositorio)
- Entorno virtual (`venv`)
- Navegador Web

### 🛠️ Instalación:

1. Clona el repositorio o descarga los archivos
2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Cargar la base de datos:

   - Abre **phpMyAdmin** y crea una base de datos nueva llamada `ferremas`
   - Luego, ve a la pestaña **"Importar"** y selecciona el archivo `ferremas_plus.sql` incluido en este repositorio

5. Crea el usuario administrador ejecutando:

   ```bash
   python crear_admin.py
   ```

6. Configura el archivo `.env` en la raíz del proyecto (en caso de ser necesario):

   ```env
   DATABASE_URL=mysql+pymysql://root:tu_clave@localhost/ferremas
   API_KEY=clave_webpay_entregada
   RETURN_URL=https://TU_URL_PUBLICA.ngrok.io/webpay/retorno
   WEB_PAY_URL_RETURN=https://TU_URL_PUBLICA.ngrok.io/pago_ex.html
   ```

---

### ▶️ Iniciar el sistema:

```bash
.\start_ferreplus.bat
```

Este script:
- Inicia `ngrok` para exponer tu app públicamente
- Inicia FastAPI (modo `uvicorn`)
- Imprime la URL pública en consola

---

### 🌐 Accede en tu navegador:

```
https://TU_URL_PUBLICA.ngrok.io/
```

Desde ahí puedes:
- Ver productos
- Registrarte como cliente
- Comprar con WebPay
- Credenciales WebPay
   Numero tarjeta: 4051 8856 0044 6623
   MM/AA: cualquiera
   CVV: 123
   Rut: 11.111.111-1
   Clave: 123
- Iniciar sesión como admin o vendedor
- Credenciales admin
   Correo: admin@ferremas.cl Contraseña: admin123
- Credenciales cliente
   Correo: Tiagopzk00@gmail.com Contraseña: cliente123


---

### 🧪 Pruebas y validaciones

- Validaciones de stock
- Manejo de tokens WebPay
- Redirecciones seguras
- Integración completa cliente → carrito → pago → backend
- API lista para ser usada desde Postman o frontend externo

---

### 👨‍👩‍👧‍👦 Roles del sistema

- **Cliente**: compra productos y recibe descuentos
- **Administrador**: gestiona usuarios y reportes
- **Vendedor**: aprueba pedidos y coordina entregas
- **Bodeguero**: despacha productos
- **Contador**: confirma pagos por transferencia

---

## 📩 Contacto

Autor: Hector Shulcz - Ignacio Lopez - Josue Garcia
Correo: [jos.garciag@duocuc.cl]  
Sección: 002D | Grupo: 6
