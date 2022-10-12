
import configparser
from tkinter import E
import requests
import pandas as pd
from datetime import datetime
import sys
import json
import configparser


class weather():

    def __init__(self):
        self.configfile = './weather/config.ini'
        self.filename = 'sandnes'

    def get_api_key(self):
        config = configparser.ConfigParser()
        config.read(self.configfile)
        return config['openweathermap']['api']

    def get_weather(self, api_key, location):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
            r = requests.get(url)
            r.raise_for_status()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
        return r.json()

    def get_filename(self):
        now = datetime.now()
        dato = now.strftime("%m-%d-%Y")
        file = self.filename
        return f"{file}.csv"

    def get_now_date(self):
        date = datetime.now()
        return date


def get_air_pollution(api_key, lat, lon):
    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        r = requests.get(url)
    except requests.HTTPError as e:
        print(f"[!] Exception caught: {e}")
    return r.json()


# Make a varible if class
test = weather()

# Return value from api and put them into dataframe and csv file
weather = (test.get_weather(test.get_api_key(), 'Sandnes'))
temp = weather['main']['temp']
for i in weather['weather']:
    weather_type = i['description']
windspeed = weather['wind']['speed']
city = weather['name']
air = (get_air_pollution(test.get_api_key(), 58.8, 5.7))
for i in air['list']:
    quality = i['main']['aqi']


df = pd.DataFrame(
    {'tmp': temp, 'wind': windspeed, 'air': quality, 'city': city, 'weather_type': weather_type, 'dato': test.get_now_date()}, index=[0])

df.to_csv(f'./weather/files/{test.get_filename()}', mode='a', header=False)
# with open(f"./weather/results-{dato}.csv", "a+") as csvfile:
#     fieldnames = ['temp', 'wind', "air_po", 'dato', 'name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(
#         {'temp': weather['main']['temp'], 'wind': weather['wind']['speed'], 'air_po': quality, 'dato': date, 'name': weather['name']})
