from flask import Flask, render_template

app = Flask(__name__)


@app.after_request
def no_cache(response):
    if response.mimetype == "text/html":
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
    return response


@app.get("/")
def inicio():
    return render_template("index.html")


@app.get("/<path:ruta>")
def pagina(ruta):
    # The agenda is a single page; keep its entry point available on nested paths.
    return render_template("index.html")


if __name__ == "__main__":
    import os

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
