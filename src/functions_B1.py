def imprimir_resultado(registro, actual):
    total = registro["1"] + registro["2"] + registro["3"]
    if total == 0:
        print(
            f"""año: {actual}
    No hay datos disponibles para calcular porcentajes.
    -------------------------------
    """
        )
    else:
        leidos = (registro["1"] * 100) / total
        no_leidos = 100 - leidos
        print(
            f"""año: {actual}
    leidos: {leidos:.2f} 
    no_leidos: {no_leidos:.2f}
    -------------------------------
    """
        )


def obtener_trimestre_mas_alto(anio, dataset, i_año, i_tri):
    trimestres = []

    # Recorrer el dataset y filtrar por el año dado
    for fila in dataset:
        if fila[i_año] == anio:
            trimestres.append(fila[i_tri])

    return max(trimestres)
