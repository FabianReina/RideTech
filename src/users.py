# src/users.py

usuarios = []

def registrar_usuario(username=None, password=None):
    username = username or "usuario_default"
    password = password or "123456"

    # VALIDACIÓN UNIVERSAL DE DUPLICADOS:
    # Compara el 'username' que entra contra todos los que ya existen en la lista
    for u in usuarios:
        if u["username"] == username:
            # Si ya existe, retornamos el usuario encontrado y no agregamos nada
            return u 

    # Si el bucle termina y no encontró duplicados, creamos el nuevo
    usuario = {
        "username": username,
        "password": password,
        "puntos": 0
    }

    usuarios.append(usuario)
    return usuario

def autenticar_usuario(username, password):
    for user in usuarios:
        if user["username"] == username and user["password"] == password:
            return True
    return False