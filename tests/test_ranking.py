from src.ranking import ordenar_por_puntos


def test_ordenar_por_puntos_descendente():
    usuarios = [
        {"username": "a", "puntos": 10},
        {"username": "b", "puntos": 30},
        {"username": "c", "puntos": 20},
    ]

    ordenados = ordenar_por_puntos(usuarios)

    assert ordenados[0]["puntos"] == 30
    assert ordenados[1]["puntos"] == 20
    assert ordenados[2]["puntos"] == 10


def test_lista_vacia():
    assert ordenar_por_puntos([]) == []


def test_un_solo_usuario():
    usuarios = [{"username": "solo", "puntos": 5}]
    ordenados = ordenar_por_puntos(usuarios)
    assert len(ordenados) == 1