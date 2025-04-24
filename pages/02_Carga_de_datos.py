import streamlit as st
from src.functions_stl import min_y_max
from src.functions_stl import min_y_max_dataset
from src.crear_dataset import ejecutar
from pathlib import Path


carpeta = Path("DATA")
print(carpeta)


st.button("Apretar", on_click=ejecutar(carpeta))
