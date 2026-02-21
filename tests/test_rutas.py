from src.rutas import agregar_ruta, rutas


def test_agregar_ruta_normal():
    ruta = agregar_ruta("Ruta Medellin", "Alta")
    assert ruta["nombre"] == "Ruta Medellin"
    assert ruta["dificultad"] == "Alta"


def test_agregar_ruta_nombre_nulo():
    ruta = agregar_ruta(None, "Baja")
    assert ruta["nombre"] == "Ruta Default"


def test_agregar_ruta_dificultad_nula():
    ruta = agregar_ruta("Ruta Cali", None)
    assert ruta["dificultad"] == "Media"


def test_ruta_se_agrega_a_lista():
    cantidad_inicial = len(rutas)
    agregar_ruta("Nueva Ruta", "Media")
    assert len(rutas) == cantidad_inicial + 1