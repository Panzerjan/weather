#Import Modules
import pandas as pd
import json

from functions import lake, files, date
from api import get_api
from functions import keyVault



# set variables
nve_url = keyVault.KeyVault().getSecret('urlNve')
nve_sisteuke = "HentOffentligDataSisteUke"
omraade = "HentOmråder"
his_path = './nve/his_files'
new_path = './nve/file/'

# Get Magasin statestik siste uken
nve = get_api.api(f'{nve_url}')
nve_uke = nve.get_nve(f'{nve_sisteuke}')

# set Filename
dato = date().get_date()

file = files().set_filename(f'{nve_sisteuke}_{dato}', "json")


with open(f'{new_path}{file}', 'w', encoding='utf-8') as f:
    json.dump(nve_uke, f, ensure_ascii=False, indent=4)


# Connect to lake
lake.initialize_storage_account('janistgac', lake.storage_account_key())



# Upload file to lake
lake.upload_file(f'{file}', 'nve',
                f"{new_path}{file}")

#move file to historical folder
files.move_file(new_path, his_path, file)