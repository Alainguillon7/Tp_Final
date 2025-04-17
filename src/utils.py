def get_indice(filas, columna):
    """
    Obtiene el indice de la columna deseada en el encabezado del archivo.

    Parametros:
        filas: lista de filas del archivo, incluyendo el encabezado.
        columna: nombre de la columna que se quiere buscar.

    Retorna:
        el indice de la columna en el encabezado.
    """
    encabezado = filas[0]
    # Si no existe la columna CH04, se lanza un error
    if columna not in encabezado:
        raise ValueError(f"La columna {columna} no se encuentra en el encabezado.")
    # Se obtiene el indice de la columna
    i = encabezado.index(columna)
    return i
