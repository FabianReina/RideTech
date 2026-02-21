def ordenar_por_puntos(usuarios):
    return sorted(
        usuarios,
        key=lambda x: x["puntos"],
        reverse=True
    )