from fastapi import FastAPI

app = FastAPI()

@app.get("/hola")
def hola():
    return {"mensaje": "Hola Mundo"}

@app.get("/hola/{nombre}")
def hola_nombre(nombre: str):

    return {"mensaje": f"Hola {nombre}"}

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a mi API"}