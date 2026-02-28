from fastapi import FastAPI
from src.exceptions import UserAlreadyExistsError, InvalidDataError, AuthenticationError, RouteError
from users import registrar_usuario
from rutas import agregar_ruta

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Mi API está funcionando"}

@app.post("/usuarios")
def crear_usuario(nombre: str, email: str):
    try:
        usuario = registrar_usuario(nombre, email)
        return {"usuario": usuario}
    except UserAlreadyExistsError as e:
        return {"error": str(e)}

@app.post("/rutas")
def crear_ruta(nombre: str, distancia: int, dificultad: str):
    try:
        ruta = agregar_ruta(nombre, distancia, dificultad)
        return {"ruta": ruta}
    except RouteError as e:
        return {"error": str(e)}