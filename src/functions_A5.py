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
    from utils import get_indice

    i1 = get_indice(filas[0], columna1)
    i2 = get_indice(filas[0], columna2)
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
