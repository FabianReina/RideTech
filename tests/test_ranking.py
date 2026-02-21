from src.ranking import ordenar_por_puntos


def test_ordenar_por_puntos():

    usuarios = [
        {"nombre": "A", "puntos": 50},
        {"nombre": "B", "puntos": 150},
        {"nombre": "C", "puntos": 100},
    ]

    ranking = ordenar_por_puntos(usuarios)

    assert ranking[0]["nombre"] == "B"
    assert ranking[1]["nombre"] == "C"
    assert ranking[2]["nombre"] == "A"


def test_lista_vacia():

    ranking = ordenar_por_puntos([])

    assert ranking == []