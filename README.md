# Proyecto Flask + MySQL para Railway

Aplicación CRUD básica para registrar, listar y eliminar aprendices.

## Archivos
- `app.py`: aplicación Flask y creación automática de la tabla.
- `templates/index.html`: interfaz.
- `requirements.txt`: dependencias.
- `Procfile`: comando de inicio para Railway.

## Creación automática de la tabla
Al iniciar `app.py`, se ejecuta `preparar_bd()`. Esta función conecta con la base de datos configurada y ejecuta `CREATE TABLE IF NOT EXISTS aprendices`. No elimina registros existentes.

## Variables de entorno
La aplicación acepta `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` y `SECRET_KEY`. También acepta directamente los nombres `MYSQLHOST`, `MYSQLPORT`, `MYSQLUSER`, `MYSQLPASSWORD` y `MYSQLDATABASE` que proporciona Railway.

## Ejecutar localmente
1. Crear una base de datos MySQL llamada `institucion` en un servidor local.
2. Crear un entorno virtual e instalar: `pip install -r requirements.txt`.
3. Configurar las variables `DB_*` (por ejemplo, en un archivo `.env`, cargándolas en el entorno).
4. Ejecutar `python app.py`.
5. Abrir `http://127.0.0.1:5000`.

La tabla `aprendices` se crea automáticamente. No se necesita MySQL Workbench para crear la tabla; el servidor MySQL local sí debe estar instalado y ejecutándose.

## Desplegar en Railway
1. Subir esta carpeta a un repositorio de GitHub.
2. En Railway crear un proyecto y añadir un servicio MySQL.
3. Añadir un servicio desde GitHub y seleccionar el repositorio.
4. En el servicio Flask, configurar las variables `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD` y `DB_NAME` usando los valores/ referencias del servicio MySQL (`MYSQLHOST`, `MYSQLPORT`, `MYSQLUSER`, `MYSQLPASSWORD`, `MYSQLDATABASE`).
5. Crear `SECRET_KEY` con un valor largo y aleatorio.
6. Desplegar y generar un dominio público desde Settings > Networking > Generate Domain.

No se debe crear manualmente la tabla. El servicio MySQL de Railway crea/provisiona la base de datos; `app.py` crea la tabla al arrancar.
