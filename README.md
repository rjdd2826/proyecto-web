# Agenda Virtual

Agenda diaria con login local, calendario mensual y gestión de actividades.

## Datos y privacidad

Esta app no usa base de datos ni envía datos a un servidor. Las cuentas (correo y hash de contraseña), actividades y perfil se guardan en el `localStorage` de cada navegador. No se sincronizan entre dispositivos. La recuperación de contraseña solo actualiza el acceso local de ese navegador.

Los registros de aprendices de la versión anterior permanecen en la base de datos, pero esta aplicación ya no se conecta a ella ni los muestra.

## Ejecutar localmente

1. Instala las dependencias: `pip install -r requirements.txt`.
2. Ejecuta `python app.py`.
3. Abre `http://127.0.0.1:5000`.

## Railway

El servicio se despliega desde la rama `main` de este repositorio y arranca con Gunicorn mediante `Procfile`.
