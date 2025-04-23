def traducir_3(IV6,IV7,IV8,IV9,IV11,MATERIAL_TECHUMBRE):
    """convierte el digito en su equivalente en string"""
    if IV6 =="3" or IV8 == "2" or IV9 == "3" or IV11 == "4" or MATERIAL_TECHUMBRE == "Material precario":
        aux = "INSUFICIENTE"
    elif IV6 in ["1", "2"] and IV8 == "1" and IV9 in ["1", "2"] and IV11 in ["2", "3"] and MATERIAL_TECHUMBRE in ["Material durable", "Material precario"]:
        aux = "REGULAR"
    #elif IV6 == "1" and IV8 == "1" and IV9 == "1" and MATERIAL_TECHUMBRE == "Material durable" and (IV7 in ["2"] and IV11 in ["2"]):
    elif IV6 == "1" and IV8 == "1" and IV9 == "1" and MATERIAL_TECHUMBRE == "Material durable" and IV7 == "2" and IV11 == "2":
        aux = "SALUDABLE"
    elif IV6 == "1" and IV7 == "1" and IV8 == "1" and IV9 == "1" and IV11 == "1" and MATERIAL_TECHUMBRE == "Material durable":        
        aux="BUENA"
    else:
        aux="invalido"
    return aux


def agregar_columna_3(datos):
    """agrega a la lista la columna con sus datos"""
    from utils import get_indice

    encabezado = datos[0]
    encabezado.append("CONDICION_DE_HABITABILIDAD")
    IV6 =  get_indice(encabezado, "IV6")
    IV7  =  get_indice(encabezado, "IV7")
    IV8  = get_indice(encabezado, "IV8")
    IV9  = get_indice(encabezado, "IV9")
    IV11   = get_indice(encabezado, "IV11")
    MATERIAL_TECHUMBRE = get_indice(encabezado, "MATERIAL_TECHUMBRE")
    for row in datos[1:]:
        # me aseguro de que el valor sea un digito
        if row[IV6].isdigit() and row[IV7].isdigit() and row[IV8].isdigit() and row[IV9].isdigit() and row[IV11].isdigit():
            condicion = traducir_3(row[IV6],row[IV7],row[IV8],row[IV9],row[IV11],row[MATERIAL_TECHUMBRE])           
        else:
            condicion = "invalido"
        row.append(condicion)