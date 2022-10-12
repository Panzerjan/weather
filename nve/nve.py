import requests
import pandas as pd
import sys
import shutil
import json

sys.path.append( './functions/' )
from config import files , lake


# set variables
nve_sisteuke = "HentOffentligDataSisteUke"
omraade = "HentOmråder"
his_path = './nve/his_files'
new_path = './nve/file/'

class nve_api():


    def get_weather(self, api_req):
        try:
            url = f"https://biapi.nve.no/magasinstatistikk/api/Magasinstatistikk/{api_req}"
            r = requests.get(url)
            r.raise_for_status()
        except requests.HTTPError as e:
            print(f"[!] Exception caught: {e}")
        return r.json()



data = nve_api().get_weather(nve_sisteuke)
file = files().set_filename(nve_sisteuke, "json")



with open(f'{new_path}{file}', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Connect to lake
lake.initialize_storage_account('janistgac', lake.storage_account_key())

# Upload file to lake
lake.upload_file(f'{file}', 'nve',
                 f"{new_path}{file}")

# move file to historical folder
files.move_file(new_path, his_path, file)