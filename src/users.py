usuarios = []

def registrar_usuario(nombre, email):
    if not nombre or not email:
        raise ValueError("Datos incompletos")

    usuario = {
        "nombre": nombre,
        "email": email,
        "puntos": 0
    }

    usuarios.append(usuario)
    return usuario


def buscar_usuario(email):
    for u in usuarios:
        if u["email"] == email:
            return u
    return None