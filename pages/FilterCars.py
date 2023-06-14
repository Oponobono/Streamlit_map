import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd

# Crear datos de ejemplo
marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Camry', 'Civic', 'F-150', 'Silverado', 'Altima', 'X5', 'C-Class', 'A4', 'Jetta', 'Elantra']
anios = [2018, 2020, 2019, 2017, 2016, 2021, 2018, 2020, 2019, 2017]
precios = np.random.randint(15000, 50000, 10)

# Crear DataFrame con los datos
df_autos = pd.DataFrame({'marca': marcas, 'modelo': modelos, 'anio': anios, 'precio': precios})

# Mostrar el DataFrame


st.title("Precios carros ")

df_autos