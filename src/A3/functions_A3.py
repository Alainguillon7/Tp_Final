def crear_columna(filas):
    """
    Crea una lista con una nueva columna (CH04STR) string con el sexo de un individuo segun la columna asociada (CH04)

    Parámetros:
        filas: lista de filas del archivo, incluyendo el encabezado.


    Retorna:
        Una lista con la nueva columna, incluyendo encabezado.
    """

    encabezado = filas[0]
    # Si no existe la columna CH04, se lanza un error
    if "CH04" not in encabezado:
        raise ValueError("La columna 'CH04' no se encuentra en el encabezado.")
    # Obtener la posicion de la columna CH04
    i = encabezado.index("CH04")
    columna = ["CH04STR"]
    for fila in filas[1:0]:
        if fila[i] == "1":
            columna.append("Hombre")
        elif fila[i] == "2":
            columna.append("Mujer")
        else:
            columna.append("No Especificado")

    return columna, i
