import pandas as pd
import simplekml

# Ler o arquivo Excel
df = pd.read_excel('links.xlsx')

# Inicializar o objeto KML
kml = simplekml.Kml()

# Função para adicionar marcadores ao KML
def add_placemarks(kml, df):
    for index, row in df.iterrows():
        if pd.notna(row['Latitude']) and pd.notna(row['Longitude']):
            kml.newpoint(name=row['Google Maps Link'], coords=[(row['Longitude'], row['Latitude'])])

# Adicionar marcadores ao KML
add_placemarks(kml, df)

# Salvar o KML
kml.save('arquivo.kml')
