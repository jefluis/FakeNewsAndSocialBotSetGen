import pandas as pd
import re

# Read the Excel file
df = pd.read_excel('Links.xlsx')

# Function to extract coordinates from Google Maps links
def extract_coordinates(url):
    # Regular expression to extract coordinates from the link
    regex = r"@(-?\d+\.\d+),(-?\d+\.\d+)"
    match = re.search(regex, url)
    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return latitude, longitude
    else:
        return None, None

# Apply the function to each row of the DataFrame
df['Latitude'], df['Longitude'] = zip(*df['Google Maps Link'].apply(extract_coordinates))

# Save the updated DataFrame to a new Excel file
df.to_excel('coordinates_extracted.xlsx', index=False)


