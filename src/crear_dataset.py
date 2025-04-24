import csv
from pathlib import Path
from src.utils import get_indice

# Ruta fija basada en la ubicación de este archivo .py
BASE_DIR = Path(__file__).resolve().parent.parent


def crear_dataset_ind(carpeta):

    archivos = list(carpeta.glob("usu_individual_T*.txt"))
    lista = []
    encabezado = [None]
    for archivo in archivos:
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            # Leer el encabezado solo una vez
            if encabezado == [None]:
                encabezado = next(reader)  # 1er caso, se guarda el encabezado
            else:
                next(reader)  # Saltea el encabezado si ya fue guardado
            # Guardar la data en la lista
            lista.extend(list(reader))
    i_año = encabezado.index("ANO4")
    i_tri = encabezado.index("TRIMESTRE")
    list_dataset = sorted(lista, key=lambda x: ((x[i_año]), (x[i_tri])))
    path_dataset = BASE_DIR / "dataset_individuos.txt"
    with open(path_dataset, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(encabezado)
        writer.writerows(list_dataset)
    # DataSet creado


def crear_dataset_hogar(carpeta):

    archivos = list(carpeta.glob("usu_hogar_T*.txt"))
    lista = []
    encabezado = [None]
    for archivo in archivos:
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            # Leer el encabezado solo una vez
            if encabezado == [None]:
                encabezado = next(reader)  # 1er caso, se guarda el encabezado
            else:
                next(reader)  # Saltea el encabezado si ya fue guardado
            # Guardar la data en la lista
            lista.extend(list(reader))
    i_año = encabezado.index("ANO4")
    i_tri = encabezado.index("TRIMESTRE")
    list_dataset = sorted(lista, key=lambda x: ((x[i_año]), (x[i_tri])))
    path_dataset = BASE_DIR / "dataset_hogar.txt"
    with open(path_dataset, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(encabezado)
        writer.writerows(list_dataset)
    # DataSet creado


def ejecutar(carpeta):
    crear_dataset_ind(carpeta)
    crear_dataset_hogar(carpeta)
