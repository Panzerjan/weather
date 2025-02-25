# Import modules
from importlib.metadata import files
from common.lake import Lake  # Ensure you're importing the class correctly
from common import files, Dato
from common.api import get_api
import pandas as pd
from common.keyvault import secrets
from common.server import sql

# Connect to SQL Server
connect = sql.Database()

# Set variables
url_weather = secrets.KeyVault().getSecret('urlWeather')
url_air = secrets.KeyVault().getSecret('urlAir')
weather_path = './files/weather/'

# Get weather information for Sandnes
weather = get_api.api(f'{url_weather}')
weather_today = weather.get_weather(weather.get_api_key(), 'Sandnes')

# Get air pollution
air = get_api.api(f'{url_air}')
air_today = air.get_air_pollution(air.get_api_key(), 58.8, 5.7)

# Extract values from API response
temp = weather_today['main']['temp']
for i in weather_today['weather']:
    weather_type = i['description']
windspeed = weather_today['wind']['speed']
city = weather_today['name']

# Get Air Pollution
for i in air_today['list']:
    quality = i['main']['aqi']

# Create a DataFrame
df = pd.DataFrame({
    'tmp': temp, 
    'wind': windspeed, 
    'air': quality, 
    'city': city, 
    'weather_type': weather_type, 
    'dato': Dato().get_now_date()
}, index=[0])

# Insert DataFrame into SQL Server
connect.InsertDf(df, 'weather')

# Create file name
file_weather = files().set_filename('sandnes', "csv")

# Append DataFrame to CSV file
df.to_csv(f'{weather_path}{file_weather}', mode='a', header=False)
print(f"✅ {file_weather} is written to {weather_path}")

# Initialize Lake Storage
Lake.initialize_storage_account('janistgac')

# Upload the file to the lake
Lake.upload_file(file_weather, 'OpenW', f"{weather_path}{file_weather}")
