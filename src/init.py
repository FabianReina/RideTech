from users import registrar_usuario
from rutas import agregar_ruta


usuario1 = registrar_usuario("Fabian", "fabian@gmail.com")

ruta1 = agregar_ruta("Medellín - Guatapé", 120, "Media")

print(usuario1)
print(ruta1)