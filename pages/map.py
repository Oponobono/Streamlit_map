import folium

# Crear un mapa centrado en Colombia
mapa_colombia = folium.Map(location=[4.5709, -74.2973], zoom_start=6)

# Crear una función para resaltar el departamento seleccionado
def resaltar_departamento(departamento):
    # Código de colores para resaltar el departamento seleccionado
    colores = {'antioquia': 'green', 'atlantico': 'blue', 'bolivar': 'red', 'boyaca': 'purple', 'caldas': 'orange'}
    
    # Verificar si el departamento está en la lista de colores
    if departamento.lower() in colores:
        # Crear un GeoJson que representa el departamento seleccionado y resaltarlo con el color correspondiente
        folium.GeoJson(f'departamentos/{departamento.lower()}.geojson', name=departamento.upper(),
                       style_function=lambda x: {'fillColor': colores[departamento.lower()], 'color': 'black', 'weight': 1.5}).add_to(mapa_colombia)

# Resaltar el departamento de Antioquia
dp = 'antioquia'
resaltar_departamento(dp)

# Guardar el mapa como un archivo HTML
mapa_colombia.save('mapa_colombia.html')
