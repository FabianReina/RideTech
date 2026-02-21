def ordenar_por_puntos(lista_usuarios):
    return sorted(lista_usuarios, key=lambda x: x["puntos"], reverse=True)