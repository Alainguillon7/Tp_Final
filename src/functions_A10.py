def traducir_3(IV6, IV7, IV8, IV9, IV11, MATERIAL_TECHUMBRE):
    # BUENA: todos los mejores valores posibles
    if IV6 == "1" and IV7 == "1" and IV8 == "1" and IV9 == "1" and IV11 == "1" and MATERIAL_TECHUMBRE == "Material durable":
        return "BUENA"
    
    # SALUDABLE: leve diferencia con respecto a la BUENA, pero aún bien mantenida
    if IV6 == "1" and IV8 == "1" and IV9 == "1" and IV11 == "2" and IV7 == "2" and MATERIAL_TECHUMBRE == "Material durable":
        return "SALUDABLE"

    # REGULAR: incluye muchos de los que antes caían como inválidos
    if IV6 in ["1", "2"] and IV7 in ["1", "2", "3"] and IV8 == "1" and IV9 in ["1", "2"] and IV11 in ["1", "2", "3"] and MATERIAL_TECHUMBRE in ["Material durable", "Material precario"]:
        return "REGULAR"

    # INSUFICIENTE: todo lo que no cumple con ninguna de las anteriores
    return "INSUFICIENTE"

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
        # Conjunto para guardar las filas inválidas ya impresas
    filas_invalidas_imprimidas = set()
    for row in datos[1:]:
        # me aseguro de que el valor sea un digito
        if row[IV6].isdigit() and row[IV7].isdigit() and row[IV8].isdigit() and row[IV9].isdigit() and row[IV11].isdigit():
            condicion = traducir_3(row[IV6],row[IV7],row[IV8],row[IV9],row[IV11],row[MATERIAL_TECHUMBRE])           
        else:
            condicion = "invalido"
        if condicion == "invalido" and tuple((row[IV6], row[IV7], row[IV8], row[IV9], row[IV11], row[MATERIAL_TECHUMBRE])) not in filas_invalidas_imprimidas:
            filas_invalidas_imprimidas.add(tuple((row[IV6], row[IV7], row[IV8], row[IV9], row[IV11], row[MATERIAL_TECHUMBRE])))  # Guardamos los valores clave de la fila como impresa
            # Imprimir los valores relevantes
            print(f"Fila inválida encontrada en los valores: IV6: {row[IV6]}, IV7: {row[IV7]}, IV8: {row[IV8]}, IV9: {row[IV9]}, IV11: {row[IV11]}, MATERIAL_TECHUMBRE: {row[MATERIAL_TECHUMBRE]}")
        row.append(condicion)