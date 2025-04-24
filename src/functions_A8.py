from utils import get_indice


def convertir(V4):
    """convierte el digito en su equivalente en string"""
    if V4 >= 1 and V4 <= 4:
        aux = "Material durable"
    elif V4 >= 5 and V4 <= 7:
        aux = "Material precario"
    elif V4 == 9:
        aux = "No aplica"
    return aux


def agregar_columna(datos):
    """agrega a la lista la columna con sus datos"""
    encabezado = datos[0]
    encabezado.append("MATERIAL_TECHUMBRE")
    V4 = get_indice(encabezado, "IV4")
    for row in datos[1:]:
        # me aseguro de que el valor sea un digito
        if row[V4].isdigit():
            V4_value = int(row[V4])
            resultado = convertir(V4_value)
        else:
            resultado = "invalido"
        row.append(resultado)
