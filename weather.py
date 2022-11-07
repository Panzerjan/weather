# import modules

from importlib.metadata import files
from functions import lake, files, date
from api import get_api
import pandas as pd
from functions import keyVault




# set variables
url_weather= keyVault.KeyVault().getSecret('urlWeather')
url_air = keyVault.KeyVault().getSecret('urlAir')
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
    {'tmp': temp, 'wind': windspeed, 'air': quality, 'city': city, 'weather_type': weather_type, 'dato': date().get_now_date()}, index=[0])

# Create file names
file_weather = files().set_filename('sandnes', "csv")

df.to_csv(f'{weather_path}{file_weather}', mode='a', header=False)
print(f'{file_weather} is written to {weather_path}')

# from functions import config

# # Connect to lake
lake.initialize_storage_account('janistgac', lake.storage_account_key())

# now = datetime.now()
# dato = now.strftime("%m-%d-%Y")
# file_name = f"results-{dato}.csv"

lake.upload_file(f'sandnes.csv', 'OpenW',
                  f"./files/weather/sandnes.csv")
