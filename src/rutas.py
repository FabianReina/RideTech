from src.exceptions import RouteError

rutas = []


def agregar_ruta(nombre: str, km: float, nivel: str):

    if km <= 0:
        raise RouteError("Kilometraje inválido")

    ruta = {
        "nombre": nombre,
        "km": km,
        "nivel": nivel
    }

    rutas.append(ruta)

    return ruta