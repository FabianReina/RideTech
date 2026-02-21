rutas = []

def agregar_ruta(nombre=None, dificultad=None):
    nombre = nombre or "Ruta Default"
    dificultad = dificultad or "Media"

    ruta = {
        "nombre": nombre,
        "dificultad": dificultad
    }

    rutas.append(ruta)
    return ruta