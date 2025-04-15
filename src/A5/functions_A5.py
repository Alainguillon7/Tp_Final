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
    # Obtener la posicion de la columna CH04
    i = encabezado.index(columna)
    return i


def crear_columna(filas, columna1, columna2, columna_nueva, tabla):
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
    i1 = get_indice(filas, columna1)
    i2 = get_indice(filas, columna2)
    nueva = []
    nueva.append(columna_nueva)

    for fila in filas[1:]:
        num1 = fila[i1]
        num2 = fila[i2]
        if (num1.isdigit()) and (num2.isdigit()):
            if num1 == "1":
                nueva.append(tabla.get(int(num1)).get(int(num2), "Sin informacion"))
            else:
                nueva.append(tabla.get(int(num1), "Sin informacion"))
        else:
            nueva.append("Sin informacion")
    return nueva


def traduccion_columna_doble(path_dataset, columna1, columna2, columna_nueva, tabla):
    """
    Crea una nueva columna en el archivo CSV con la traduccion de los valores de la columna original.
    """
    import csv

    with open(path_dataset, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        filas = list(reader)
    if (columna_nueva) not in filas[0]:
        # crear una lista con los datos
        columna = crear_columna(filas, columna1, columna2, columna_nueva, tabla)
        i = get_indice(filas, columna2)

        for j, fila in enumerate(filas):
            fila.insert(i + 1, columna[j])

        with open(path_dataset, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerows(filas)
