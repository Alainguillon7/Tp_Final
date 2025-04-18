import streamlit as st
from src.functions_stl import min_y_max
from src.functions_stl import min_y_max_dataset
from src.crear_dataset import ejecutar
from src.utils import get_indice
from pathlib import Path



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


carpeta = Path("DATA")
print (carpeta)




st.button('Apretar',on_click=ejecutar(carpeta))