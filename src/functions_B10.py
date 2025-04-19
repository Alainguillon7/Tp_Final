from utils import get_indice
from functions_B7 import traducir


def imprimir_encabezado(aglomerado1, aglomerado2):
    """
    Imprime el encabezado de la tabla de resultados.
    """
    from functions_B7 import traducir

    print(f"Secundario incompleto en {traducir(aglomerado1)} y {traducir(aglomerado2)}")
    print("-" * 180)
    print(
        f"{'Año':^10}|{'Trimestre':^12}|{traducir(aglomerado1):^25}|{traducir(aglomerado2):^25}|",
        end="",
    )

    print()
    print("-" * 180)


def imprimir_resultado(año, tri, datos):
    """
    Imprime el resultado por año y trimestre.
    """
    print(f"{año:^10}|{tri:^12}|", end="")
    for valor in datos.values():
        print(f"{str(valor):^25}|", end="")
    print()


def agrupar_por_trimestre(filas, i_año, i_tri, i_edu, i_cant):
    datos = {}
    for fila in filas:
        año = fila[i_año]
        tri = fila[i_tri]
        clave = (año, tri)
        if clave not in datos:
            datos[clave] = {"Secundario incompleto": 0, "total": 0}

        datos[clave]["total"] += int(fila[i_cant])
        if fila[i_edu] == "Secundario incompleto":
            datos[clave]["Secundario incompleto"] += int(fila[i_cant])
    return datos


def calcular_porcentaje(registro):
    try:
        return round((registro["Secundario incompleto"] / registro["total"]) * 100)
    except ZeroDivisionError:
        return 0.0


def crear_tabla(filas, aglomerado1, aglomerado2):
    i_aglomerado = get_indice(filas[0], "AGLOMERADO")
    i_edad = get_indice(filas[0], "CH05")
    i_edu = get_indice(filas[0], "NIVEL_ED_str")
    i_tri = get_indice(filas[0], "TRIMESTRE")
    i_año = get_indice(filas[0], "ANO4")
    i_cant = get_indice(filas[0], "PONDERA")

    tri = None
    año = None
    
    filas1 = list(
        filter(
            lambda x: ((x[i_aglomerado] == aglomerado1) and (x[i_edad] >= "18")),
            filas[1:],
        )
    )
    filas2 = list(
        filter(
            lambda x: ((x[i_aglomerado] == aglomerado2) and (x[i_edad] >= "18")),
            filas[1:],
        )
    )

    datos1 = agrupar_por_trimestre(filas1, i_año, i_tri, i_edu, i_cant)
    datos2 = agrupar_por_trimestre(filas2, i_año, i_tri, i_edu, i_cant)

    imprimir_encabezado(aglomerado1, aglomerado2)

    # Obtenemos claves comunes (año, trimestre) ordenadas
    claves = sorted(set(datos1.keys()) & set(datos2.keys()))

    for clave in claves:
        año, tri = clave
        porc1 = calcular_porcentaje(datos1[clave])
        porc2 = calcular_porcentaje(datos2[clave])
        imprimir_resultado(año, tri, {"agl1": porc1, "agl2": porc2})
