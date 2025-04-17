def crear_dataset_ind(carpeta):
    from pathlib import Path
    import csv
    from utils import get_indice

    archivos = list(carpeta.glob("usu_individual_T*.txt"))
    lista = []
    encabezado = [None]
    for archivo in archivos:
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            # Leer el encabezado solo una vez
            if encabezado == [None]:
                encabezado = next(reader)
            # Guardar la data en la lista
            lista.extend(list(reader))
    i_año = get_indice(encabezado, "ANO4")
    i_tri = get_indice(encabezado, "TRIMESTRE")
    list_dataset = sorted(lista[1:], key=lambda x: ((x[i_año]), (x[i_tri])))
    path_dataset = Path("..") / "dataset_individuos.txt"
    with open(path_dataset, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(encabezado)
        writer.writerows(list_dataset)
    # DataSet creado


def crear_dataset_hogar(carpeta):
    import csv
    from pathlib import Path
    from utils import get_indice

    archivos = list(carpeta.glob("usu_hogar_T*.txt"))
    lista = []
    encabezado = [None]
    for archivo in archivos:
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            # Leer el encabezado solo una vez
            if encabezado == [None]:
                encabezado = next(reader)
            # Guardar la data en la lista
            lista.extend(list(reader))
    i_año = get_indice(lista, "ANO4")
    i_tri = get_indice(lista, "TRIMESTRE")
    list_dataset = sorted(lista[1:], key=lambda x: ((x[i_año]), (x[i_tri])))
    path_dataset = Path("..") / "dataset_hogar.txt"
    with open(path_dataset, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(encabezado)
        writer.writerows(list_dataset)
    # DataSet creado
