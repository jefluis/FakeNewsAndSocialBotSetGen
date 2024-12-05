import pandas as pd
#from geopy.geocoders import Nominatim
from geopy.geocoders import Photon


# Ler o arquivo Excel
df = pd.read_excel('Links3.xlsx')

# Inicializar o geocodificador do Nominatim
#geolocator = Nominatim(user_agent="geoapiExercises")
geolocator = Photon(user_agent="measurements")

# Função para obter as coordenadas
def get_coordinates(link):
    location = geolocator.geocode(link)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Aplicar a função em cada linha do DataFrame
df['Latitude'], df['Longitude'] = zip(*df['Google Maps Link'].apply(get_coordinates))

# Salvar o resultado em um novo arquivo Excel
df.to_excel('coordenadas.xlsx', index=False)
