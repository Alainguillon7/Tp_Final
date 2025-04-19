from utils import traducir


def imprimir_resultado(registro, aglomerado):
    localidad = traducir(aglomerado)

    if registro["total"] == 0:
        print(
            f"""año: {localidad}
    No hay datos disponibles para calcular porcentajes.
    -------------------------------
    """
        )
    else:
        print(
            f"""Aglomerado: {localidad}
    Porcentaje de universitarios: {((registro['universitario'] * 100) / registro['total']):.2f} 
    -------------------------------
    """
        )
