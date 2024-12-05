import pandas as pd
from geopy.geocoders import Nominatim

# Read the Excel file
df = pd.read_excel('Links3.xlsx')

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="myGeocoder")

# Function to get latitude and longitude from Google Maps link
def get_coordinates(url):
    try:
        location = geolocator.geocode(url)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except:
        return None, None

# Apply the function to each row of the DataFrame
df['Latitude'], df['Longitude'] = zip(*df['Google Maps Link'].apply(get_coordinates))

# Save the updated DataFrame to a new Excel file
df.to_excel('coordinates_extracted.xlsx', index=False)
