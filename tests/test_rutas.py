import pytest

from src.rutas import agregar_ruta, rutas
from src.exceptions import RouteError


def setup_function():
    rutas.clear()


def test_agregar_ruta_correcta():

    ruta = agregar_ruta("Ruta Medellin", 120, "Media")

    assert ruta["nombre"] == "Ruta Medellin"
    assert ruta["km"] == 120


def test_km_invalido():

    with pytest.raises(RouteError):
        agregar_ruta("Ruta Mala", -10, "Alta")