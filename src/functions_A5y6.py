def crear_columna_doble(filas, columna1, columna2, columna_nueva, tabla, tipo="str"):
    """
    Crea una nueva columna con valores transformados según una tabla dada.

    Parámetros:
        filas: lista con los datos incluyendo encabezado.
        columna1: nombre de la primera columna de entrada.
        columna2: nombre de la segunda columna (puede ser usada según tabla).
        columna_nueva: nombre para la nueva columna.
        tabla: diccionario con las reglas de transformación.
        tipo: "str" para columnas de texto, "int" para columnas numéricas.

    Retorna:
        Lista con los valores de la nueva columna, incluyendo encabezado.
    """
    from utils import get_indice

    i1 = get_indice(filas[0], columna1)
    i2 = get_indice(filas[0], columna2)
    nueva = [columna_nueva]

    for fila in filas[1:]:
        num1 = fila[i1]
        num2 = fila[i2]
        # En caso de que sea un digito se usa, sino se establece sin informacion / 2 segun corresponda el tipo de columna (str-int)
        if num1.isdigit() and num2.isdigit():
            num1, num2 = int(num1), int(num2)
            if num1 in tabla:

                if isinstance(tabla[num1], dict):
                    valor = tabla[num1].get(
                        num2, "Sin informacion" if tipo == "str" else 2
                    )
                else:
                    valor = tabla[num1]
            else:
                valor = "Sin informacion" if tipo == "str" else 2
        else:
            valor = "Sin informacion" if tipo == "str" else 2

        nueva.append(valor)

    return nueva
