# import streamlit as st
# import pandas as pd
# import numpy as np

# # Generar 20 ubicaciones aleatorias en Medellín
# latitudes = np.random.uniform(6.1507, 6.3827, 20)
# longitudes = np.random.uniform(-75.6664, -75.3972, 20)

# # Crear un dataframe con las ubicaciones
# ubicaciones = pd.DataFrame({'LAT': latitudes, 'LON': longitudes})

# # Mostrar el dataframe en un mapa interactivo utilizando st.map
# st.title('Mapa de ubicaciones aleatorias en Medellín')
# st.map(ubicaciones)

import pandas as pd
import streamlit as st

#
st.title("Movilidad Incidentes 2022 - Medellín")

#
data = pd.read_csv('mov_inc_2022.csv')
df = pd.DataFrame(data)

#
df = df.rename(columns={'LATITUD': 'LAT'})
df = df.rename(columns={'LONGITUD': 'LON'})

#
month = st.selectbox('MES',(df["MES"].sort_values(ascending=True).unique()))
day = st.selectbox('DÍA',(df["DIA"].sort_values(ascending=True).unique()))

#
df['FECHA'] = pd.to_datetime(df['FECHA'])
filtro = (df['MES'] == month) & (df['DIA'] ==day) & (df['CLASE'] =='Choque')

#
df_filtrado = df.loc[filtro]
df_filtrado = df_filtrado.loc[:, ['LAT', 'LON']]

#
df = pd.DataFrame(
    df_filtrado,
    columns=['LAT', 'LON'])

#
cantidad_datos = df_filtrado.shape[0]
st.write("Cantidad de datos encontrados:", cantidad_datos)
#
st.map(df)
