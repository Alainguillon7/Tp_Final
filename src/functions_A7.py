def traducir(IX_TOT):
    """convierte el digito en su equivalente en string"""
    if IX_TOT == 1:
        aux = "Unipersonal"
    elif 2 <= IX_TOT <= 4:
        aux = "Nuclear"
    elif IX_TOT > 4:
        aux = "Extendido"
    return aux


def agregar_columna(datos):
    """agrega a la lista la columna con sus datos"""
    from utils import get_indice

    encabezado = datos[0]
    encabezado.append("TIPO_HOGAR")
    IX_TOT = get_indice(encabezado, "IX_TOT")
    for row in datos[1:]:
        # me aseguro de que el valor sea un digito
        if row[IX_TOT].isdigit():
            IX_TOT_value = int(row[IX_TOT])
            resultado = traducir(IX_TOT_value)
        else:
            resultado = "invalido"
        row.append(resultado)
