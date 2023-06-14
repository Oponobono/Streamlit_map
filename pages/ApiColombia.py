
import streamlit as st
import pandas as pd 
import requests

# API URL
url = "https://api-colombia.com/api/v1/Map"

# Get response
response = requests.get(url)

# Check status code
if response.status_code == 200:

    # Get data
    data = response.json()
    
    # Create list of dicts from data 
    mapas = [{
        "name": d["name"],
        "Descripcion": d["description"],
        "url": d["urlImages"] 
    } for d in data]
    
    # Create DataFrame 
    df = pd.DataFrame(mapas)
    df    

    st.image(mapas[0]['url'][0])
    st.image(mapas[1]['url'][0])
    
else:
    st.error("Ocurrió un error")