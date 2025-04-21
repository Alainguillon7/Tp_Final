def get_porcentaje(registro):
    """
    Calcula el porcentaje de un diccionario mandado por parametro

    Parametros: Diccionario con datos

    Retorna: porcenataje del dato ubicado en segunda posicion respecto a los 3 primeros datos como total
    """

    # Se excluyen los menores de 10 años del calculo de porcentaje
    total = registro["1"] + registro["2"] + registro["3"]

    # En caso de que no se registren datos devuelve un porcentaje grande que nunca sera seleccionado como menor
    if total == 0:
        return 999
    else:
        # Devuelve el porcentaje
        return (registro["2"] * 100) / total
