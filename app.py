import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "clave-local-de-desarrollo")


def obtener_conexion():
    """Conecta con MySQL usando variables de Railway o valores locales."""
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", os.environ.get("MYSQLHOST", "127.0.0.1")),
        port=int(os.environ.get("DB_PORT", os.environ.get("MYSQLPORT", "3306"))),
        user=os.environ.get("DB_USER", os.environ.get("MYSQLUSER", "root")),
        password=os.environ.get("DB_PASSWORD", os.environ.get("MYSQLPASSWORD", "")),
        database=os.environ.get("DB_NAME", os.environ.get("MYSQLDATABASE", "institucion"))
    )


def preparar_bd():
    """Crea la tabla si no existe. No borra ni modifica los registros existentes."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aprendices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(120) NOT NULL,
            correo VARCHAR(150) NOT NULL
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()

        if not nombre or not correo:
            flash("Debes escribir el nombre y el correo.", "error")
            return redirect(url_for("inicio"))

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO aprendices (nombre, correo) VALUES (%s, %s)",
            (nombre, correo)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        flash("Aprendiz registrado correctamente.", "ok")
        return redirect(url_for("inicio"))

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre, correo FROM aprendices ORDER BY id DESC")
    aprendices = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template("index.html", aprendices=aprendices)


@app.route("/eliminar/<int:id>")
def eliminar(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM aprendices WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    flash("Registro eliminado.", "ok")
    return redirect(url_for("inicio"))


# Railway inicia la aplicación y esta función prepara la tabla automáticamente.
preparar_bd()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
