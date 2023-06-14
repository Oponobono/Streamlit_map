import pandas as pd
import streamlit as st
import folium
import json
from streamlit_folium import folium_static

st.set_page_config(allow_google_maps_load=True)

# Carga de los datos del dataset (suponiendo que se tienen en un archivo CSV)
datos = pd.read_csv('homicidios_colombia.csv')

departamento_filtrado='Antioquia'

# Filtrado de datos
datos_filtrados = datos[datos['Departamento del hecho DANE'] == 'departamento_filtrado']

# Creación del mapa centrado en Colombia
mapa = folium.Map(location=[6.5568700, -75.8280600], zoom_start=6)

# Agregar marcador para cada fila de datos filtrados
for index, row in datos_filtrados.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']]).add_to(mapa)

# Mostrar el mapa
mapa

