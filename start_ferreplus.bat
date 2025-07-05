 @echo off
REM IMPORTANTE: Guarda este archivo como UTF-8 sin BOM o ANSI.
REM Asegúrate de que NO haya espacios o caracteres invisibles antes de @echo off en la primera línea.

chcp 65001 > nul
setlocal enabledelayedexpansion

title FERREPLUS + NGROK
echo Ô£¿ Iniciando Ferreplus con Ngrok...
echo ------------------------

REM 1. Activar entorno virtual
echo  Activando entorno virtual...
call venv\Scripts\activate

REM Verificar si ngrok.exe existe
if not exist ngrok.exe (
    echo ❌ Error: ngrok.exe no encontrado en el directorio actual.
    echo Por favor, asegúrate de que ngrok.exe esté en la misma carpeta que start_ferreplus.bat.
    pause
    exit /b 1
)

REM 2. Iniciar ngrok en segundo plano
echo 🚀 Iniciando ngrok en segundo plano...
start "" /min cmd /c ".\ngrok http 8000"

REM 3. Esperar y obtener URL pública desde ngrok
echo  Esperando que ngrok inicie y proporcione la URL pública...
set "NGROK_BASE_URL="
set "MAX_RETRIES=20"
set "RETRY_DELAY=3"
set "RETRY_COUNT=0"

:GET_NGROK_URL_LOOP
if !RETRY_COUNT! geq !MAX_RETRIES! (
    echo ❌ Error: No se pudo obtener la URL de ngrok después de !MAX_RETRIES! intentos.
    echo Asegúrate de que ngrok esté autenticado y funcionando correctamente.
    pause
    goto :EOF
)

for /f "usebackq tokens=*" %%i in (`powershell -Command "(Invoke-RestMethod http://127.0.0.1:4040/api/tunnels).tunnels | Where-Object {$_.proto -eq 'https'} | Select-Object -ExpandProperty public_url"`) do (
    set "NGROK_BASE_URL=%%i"
)

for /f "delims=" %%a in ("!NGROK_BASE_URL!") do set "NGROK_BASE_URL=%%a"
set "NGROK_BASE_URL=!NGROK_BASE_URL: =!"
set "NGROK_BASE_URL=!NGROK_BASE_URL:	=!"

echo Debug: Raw URL from PowerShell: "!NGROK_BASE_URL!"

if "!NGROK_BASE_URL:~0,8!" == "https://" (
    echo Ô£à URL base de ngrok obtenida: !NGROK_BASE_URL!
    goto :URL_OBTAINED
) else (
    echo 🔄 Reintentando en !RETRY_DELAY! segundos... (Intento !RETRY_COUNT!/!MAX_RETRIES!)
    timeout /t !RETRY_DELAY! > nul
    set /a RETRY_COUNT+=1
    goto GET_NGROK_URL_LOOP
)

:URL_OBTAINED
set "FINAL_RETURN_URL=!NGROK_BASE_URL!/webpay/retorno"
echo Debug: Final RETURN_URL para .env: "!FINAL_RETURN_URL!"

REM 4. Reescribir archivo .env completamente
echo 📝 Actualizando archivo .env con la nueva RETURN_URL...
(
    echo COMMERCE_CODE=597055555532
    echo API_KEY=579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C
    echo DB_USER=root
    echo DB_PASSWORD=
    echo DB_HOST=localhost
    echo DB_PORT=3306
    echo DB_NAME=ferremas
    echo RETURN_URL=!FINAL_RETURN_URL!
) > .env

echo ✅ .env actualizado con RETURN_URL: !FINAL_RETURN_URL!

REM 5. Instalar dependencias
echo 📦 Verificando e instalando dependencias (si es necesario)...
pip install -r requirements.txt > nul
echo ✅ Dependencias verificadas.

REM 6. Iniciar servidor FastAPI
echo  Iniciando servidor FastAPI en puerto 8000...
start "" http://127.0.0.1:8000
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
endlocal
