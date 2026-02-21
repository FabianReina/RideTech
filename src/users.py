# users.py

from src.exceptions import (
    UserAlreadyExistsError,
    InvalidDataError,
    AuthenticationError
)

usuarios = []


def registrar_usuario(nombre: str, email: str, password: str):

    if not nombre or not email or not password:
        raise InvalidDataError("Datos incompletos")

    if len(password) < 4:
        raise InvalidDataError("Contraseña muy corta")

    for u in usuarios:
        if u["email"] == email:
            raise UserAlreadyExistsError("El usuario ya existe")

    usuario = {
        "nombre": nombre,
        "email": email,
        "password": password,
        "puntos": 0
    }

    usuarios.append(usuario)

    return usuario


def buscar_usuario(email: str):

    for u in usuarios:
        if u["email"] == email:
            return u

    return None


def login(email: str, password: str):

    if not email or not password:
        raise InvalidDataError("Campos vacíos")

    usuario = buscar_usuario(email)

    if usuario is None:
        raise AuthenticationError("Usuario no existe")

    if usuario["password"] != password:
        raise AuthenticationError("Contraseña incorrecta")

    return usuario