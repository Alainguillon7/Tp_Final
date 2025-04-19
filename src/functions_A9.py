from utils import get_indice


def traducir_2(resultado):
    """convierte el digito en su equivalente en string"""
    if resultado < 1:
        aux = "Bajo"
    elif 1 <= resultado <= 2:
        aux = "Medio"
    elif resultado > 2:
        aux = "Alto"
    return aux


def agregar_columna_2(datos):
    """agrega a la lista la columna con sus datos"""

    encabezado = datos[0]
    encabezado.append("DENSIDAD_HOGAR")
    IX_TOT = get_indice(encabezado, "IX_TOT")
    IV2 = get_indice(encabezado, "IV2")
    for row in datos[1:]:
        # me aseguro de que el valor sea un digito
        if row[IX_TOT].isdigit() and row[IV2].isdigit():
            IX_TOT_value = int(row[IX_TOT])
            V2_value = int(row[IV2])
            resultado = int(V2_value / IX_TOT_value)
            densidad = traducir_2(resultado)
        else:
            densidad = "invalido"
        row.append(densidad)
