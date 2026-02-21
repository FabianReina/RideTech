rutas = []

def agregar_ruta(nombre, km, nivel):
    if km <= 0:
        raise ValueError("Kilometraje inválido")

    ruta = {
        "nombre": nombre,
        "km": km,
        "nivel": nivel
    }

    rutas.append(ruta)
    return ruta