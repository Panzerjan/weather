import requests
import json
import pandas as pd
import sys
from datetime import datetime

sys.path.append( './functions/' )
from config import files

nve_sisteuke = "HentOffentligDataSisteUke"
omraade = "HentOmråder"

class nve_api():


    def get_weather(self, api_req):
        try:
            url = f"https://biapi.nve.no/magasinstatistikk/api/Magasinstatistikk/{api_req}"
            r = requests.get(url)
            r.raise_for_status()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
        return r.json()

    def get_filename(self, file_name):
            now = datetime.now()
            dato = now.strftime("%m-%d-%Y")
            file = file_name
            return f"{file}_{dato}.json"


data = nve_api().get_weather(nve_sisteuke)
file = files().get_filename(nve_sisteuke, "json")

with open(f'./nve/file/{file}', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

