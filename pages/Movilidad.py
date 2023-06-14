import pandas as pd
import streamlit as st
import numpy as np


def Movilidad_page():
    st.title('Página de Movilidad')
    # Contenido de la página de inicio

    # Da titulo a la aplicacion 
st.title("Movilidad Incidentes 2034- Medellín")

# 
data = pd.read_csv('movilidad_incidentes_2022_gdb.csv')
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
st.map(df)

