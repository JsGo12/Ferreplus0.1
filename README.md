# Ferreplus0.1
Speed run del trabajo. Objetivo: El 4.0


 PASO A PASO 

0.1 Tener instalado: 

- Python 3.10.9 link: https://www.python.org/downloads/release/python-3109/
- XAMPP con MySQL activo y apache
- En extensiones de vs code instalar: MariaDB, y MySQLTools


1. Extraer todos los .zip ya que son las carpetas que deben estar
    dentro de la carpeta "ferreplus"
   
2. Crear entorno virtual:  python -m venv venv

3. Activar entorno virtual:  .\venv\Scripts\Activate

4. Instalar dependencias:
   pip install --upgrade pip
   pip install -r requirements.txt

5. Abrir el MyphpAdmin de XAMPP haciendo click en "admin" en MYsql XAMPP
6. Apretar en la seccion importar y seleccionar el archivo ferremas.sql

7. Abrir dos terminales, en una usar ngrok.exe con el codigo: ngrok https 8000  
7.1 Ejecutar programa con: .\start_ferreplus.bat

8. Disfruta :)

9. (Puede ser que haya que instalar el pip transbank-sdk)


Objetivos: 
.Falta comprobar si los endpoints se guardan en la base de datos
.Hay que arreglar el endpoint login ya que no devuelve token
.El pinche webpay sigue sin aparecer aunque ya esta todo instalado supuestamente
