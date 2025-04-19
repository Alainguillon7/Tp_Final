from utils import traducir, get_indice


def iniciar_registro():
    """
    Inicializa el registro de datos de los encuestados.
    """
    contador = {
        "Primario incompleto": 0,
        "Primario completo": 0,
        "Secundario incompleto": 0,
        "Secundario completo": 0,
        "Superior o universitario": 0,
        "Sin informacion": 0,
    }
    return contador


def imprimir_encabezado(datos, aglomerado):
    """
    Imprime el encabezado de la tabla de resultados.
    """

    print(f"NIvel de educacion en {traducir(aglomerado)}")
    print("-" * 180)
    print(f"{'Año':^10}|{'Trimestre':^12}|", end="")
    for clave in datos.keys():
        print(f"{clave:^25}|", end="")
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


def crear_tabla(filas, aglomerado):
    i_aglomerado = get_indice(filas[0], "AGLOMERADO")
    i_edad = get_indice(filas[0], "CH05")
    i_edu = get_indice(filas[0], "NIVEL_ED_str")
    i_tri = get_indice(filas[0], "TRIMESTRE")
    i_año = get_indice(filas[0], "ANO4")
    i_cant = get_indice(filas[0], "PONDERA")

    registro = iniciar_registro()
    tri = None
    año = None
    filas = list(
        filter(
            lambda x: ((x[i_aglomerado] == aglomerado) and (x[i_edad] >= "18")),
            filas[1:],
        )
    )

    imprimir_encabezado(registro, aglomerado)

    for fila in filas:
        if tri is None:  # Primera vez que se lee el trimestre
            tri = fila[i_tri]
            año = fila[i_año]

        if fila[i_tri] != tri:
            imprimir_resultado(año, tri, registro)
            tri = fila[i_tri]
            año = fila[i_año]
            registro = iniciar_registro()

        registro[(fila[i_edu])] += int(fila[i_cant])
    imprimir_resultado(año, tri, registro)
