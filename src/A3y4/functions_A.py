def crear_columna(filas, columna, columna_nueva, tabla):
    """
    Crea una lista con una nueva columna (CH04STR) string con el sexo de un individuo segun la columna asociada (CH04)

    Parámetros:
        filas: lista de filas del archivo, incluyendo el encabezado.
        columna: nombre de la columna que se quiere transformar.
        columna_nueva: nombre de la nueva columna que se va a crear.
        tabla: valores de conversion para la nueva columna

    Retorna:
        Una lista con la nueva columna, incluyendo encabezado.
    """
    i = get_indice(filas, columna)
    nueva = []
    nueva.append(columna_nueva)

    for fila in filas[1:]:
        num = fila[i]
        if num.isdigit():
            nueva.append(tabla.get(int(num), "Sin informacion"))
        else:
            nueva.append("Sin informacion")
    return nueva


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


def traduccion_columna(path_dataset, columna, columna_nueva, tabla):
    """
    Crea una nueva columna en el archivo CSV con la traduccion de los valores de la columna original.
    """
    import csv

    with open(path_dataset, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        filas = list(reader)
    if (columna_nueva) not in filas[0]:
        # crear una lista con los datos
        nueva = crear_columna(filas, columna, columna_nueva, tabla)
        i = get_indice(filas, columna)

        for j, fila in enumerate(filas):
            fila.insert(i + 1, nueva[j])

        with open(path_dataset, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerows(filas)
