from utils import traducir


def imprimir_resultado(total, universitario, aglomerado):
    localidad = traducir(aglomerado)

    if total == 0:
        print(
            f"""año: {localidad}
    No hay datos disponibles para calcular porcentajes.
    -------------------------------
    """
        )
    else:
        print(
            f"""Aglomerado: {localidad}
    Porcentaje de extranjeros universitarios: {((universitario * 100) / total):.2f} 
    -------------------------------
    """
        )
