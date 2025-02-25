import requests
from common.keyvault import secrets

# Class for calling different APIs
class api:
    def __init__(self, url):
        self.url = url

    def get_api_key(self):
        try:
            # Retrieve the OpenWeather API key from Azure Key Vault
            api_key = secrets.KeyVault().getSecret('apiWeather')
            if not api_key:
                raise ValueError("API key not found in Key Vault")
            return api_key
        except Exception as e:
            print(f"❌ Error retrieving API key: {e}")
            return None

    def get_nve(self, api_req):
        try:
            url = f"{self.url}{api_req}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
            return None

    def get_weather(self, api_key, location):
        try:
            url = f"{self.url}?q={location}&units=metric&appid={api_key}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
            return None

    def get_air_pollution(self, api_key, lat, lon):
        try:
            url = f"{self.url}?lat={lat}&lon={lon}&appid={api_key}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
            return None
