@echo off
REM Activar entorno virtual
call venv\Scripts\activate

REM Ejecutar el servidor FastAPI
uvicorn app.main:app --reload

pause
    