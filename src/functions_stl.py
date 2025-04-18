import os
import csv
from pathlib import Path

base_dir = os.path.dirname(os.path.abspath(__file__))
files_path = os.path.join(base_dir, '..', 'DATA')

lista = list(filter(lambda x: x.startswith('usu_hogar_T'), os.listdir(files_path)))


archivo_dataset = Path(files_path) / "dataset_hogar.txt"


def extraer_anio_trimestre(nombre):
    num = (nombre.split('_T')[1].split('.')[0])
    anio=num[1:]
    trimestre=num[0]
    return (int(anio),int(trimestre))

def min_y_max ():
    lista = list(filter(lambda x: x.startswith('usu_hogar_T'), os.listdir(files_path)))
    lista =min(lista, key=extraer_anio_trimestre) , max(lista, key=extraer_anio_trimestre)
    oracion =  ('El sistema contiene información desde 0'+lista[0][11]+'/20'+lista[0][12:14]+' hasta el '+lista[1][11]+'/20'+lista[1][12:14])
    return (oracion)

def min_y_max_dataset ():
    with open(archivo_dataset, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=";")
        filas = list(reader)
        oracion=""
        if filas:
            primera_fila = filas[1]
            ultima_fila = filas[-1]
            oracion =  ('El sistema contiene información desde 0'+primera_fila[2]+'/'+primera_fila[1]+' hasta el 0'+ultima_fila[2]+'/'+ultima_fila[1])
    return oracion
