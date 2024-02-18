# import modules

from importlib.metadata import files
from common import lake, files, Dato
from common.api import get_api
import pandas as pd
from common.keyvault import secrets
from common.server import sql


# Connect to sql server
connect = sql.Database()

# set variables
url_weather= secrets.KeyVault().getSecret('urlWeather')
url_air = secrets.KeyVault().getSecret('urlAir')
weather_path= './files/weather/'


# Get weather information for sandes
weather = get_api.api(f'{url_weather}')
weather_today = (weather.get_weather(weather.get_api_key(), 'Sandnes'))

# Get air polution
air = get_api.api(f'{url_air}')
air_today = (air.get_air_pollution(air.get_api_key(), 58.8, 5.7))

# Return value from api and put them into dataframe and csv file
temp = weather_today['main']['temp']
for i in weather_today['weather']:
    weather_type = i['description']
windspeed = weather_today['wind']['speed']
city = weather_today['name']
# Return Air Pollution
for i in air_today['list']:
    quality = i['main']['aqi']

# Create a Dataframe
df = pd.DataFrame(
    {'tmp': temp, 'wind': windspeed, 'air': quality, 'city': city, 'weather_type': weather_type, 'dato': Dato().get_now_date()}, index=[0])


#Insert Datafram into sql server
connect.InsertDf(df, 'weather')

# Create file names
file_weather = files().set_filename('sandnes', "csv")

# Append df to CSV file
df.to_csv(f'{weather_path}{file_weather}', mode='a', header=False)
print(f'{file_weather} is written to {weather_path}')


# # Connect to lake
lake.initialize_storage_account('janistgac', lake.storage_account_key())

# Upload the file to lake
lake.upload_file(f'sandnes.csv', 'OpenW',
                  f"./files/weather/sandnes.csv")
