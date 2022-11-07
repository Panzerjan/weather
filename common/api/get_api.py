import requests
import configparser
from datetime import datetime

# Class for calling different Apis
class api():

    def __init__(self, url):
        self.url=url
        self.configfile = './common/config.ini'

    def get_api_key(self):
        config = configparser.ConfigParser()
        config.read(self.configfile)
        return config['openweathermap']['api']

    def get_nve(self, api_req):
        try:
            url = f"{self.url}{api_req}"
            r = requests.get(url)
            r.raise_for_status()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
        return r.json()

    def get_weather(self, api_key, location):
        try:
            url = f"{self.url}?q={location}&units=metric&appid={api_key}"
            r = requests.get(url)
            r.raise_for_status()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
        return r.json()

    def get_air_pollution(self,api_key, lat, lon):
        try:
            url = f"{self.url}?lat={lat}&lon={lon}&appid={api_key}"
            r = requests.get(url)
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
        return r.json()

