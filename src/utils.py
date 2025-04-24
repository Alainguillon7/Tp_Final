import csv


def get_indice(encabezado, columna):
    """
    Obtiene el indice de la columna deseada en el encabezado del archivo.

    Parametros:
        filas: lista de filas del archivo, incluyendo el encabezado.
        columna: nombre de la columna que se quiere buscar.

    Retorna:
        el indice de la columna en el encabezado.
    """
    # Si no existe la columna CH04, se lanza un error
    if columna not in encabezado:
        raise ValueError(f"La columna {columna} no se encuentra en el encabezado.")
    # Se obtiene el indice de la columna
    i = encabezado.index(columna)
    return i


def get_aglomerados():
    ags = {
        "2": "Gran La Plata",
        "3": "Bahía Blanca - Cerri",
        "4": "Gran Rosario",
        "5": "Gran Santa Fé",
        "6": "Gran Paraná",
        "7": "Posadas",
        "8": "Gran Resistencia",
        "9": "Comodoro Rivadavia - Rada Tilly",
        "10": "Gran Mendoza",
        "12": "Corrientes",
        "13": "Gran Córdoba",
        "14": "Concordia",
        "15": "Formosa",
        "17": "Neuquén - Plottier",
        "18": "Santiago del Estero - La Banda",
        "19": "Jujuy - Palpalá",
        "20": "Río Gallegos",
        "22": "Gran Catamarca",
        "23": "Gran Salta",
        "25": "La Rioja",
        "26": "Gran San Luis",
        "27": "Gran San Juan",
        "29": "Gran Tucumán - Tafí Viejo",
        "30": "Santa Rosa - Toay",
        "31": "Ushuaia - Río Grande",
        "32": "Ciudad Autonoma de Buenos Aires",
        "33": "Partidos del GBA",
        "34": "Mar del Plata",
        "36": "Río Cuarto",
        "38": "San Nicolás - Villa Constitución",
        "91": "Rawson - Trelew",
        "93": "Viedma - Carmen de Patagones",
    }
    return ags


def traducir(aglomerado):
    """
    Traduce el aglomerado a su nombre correspondiente.
    """
    ags = get_aglomerados()
    return ags.get(aglomerado, aglomerado)


def lector(path_dataset):
    with open(path_dataset, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        lista = list(reader)
    return lista
