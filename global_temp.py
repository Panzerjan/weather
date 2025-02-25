import urllib.request as r
import sys
import pandas as pd
from common.server import sql

sys.path.append( './functions/' )
from common.keyvault import secrets

# set variables
url_global= secrets.KeyVault().getSecret('urlGobalTemp')

# Read the date from Gobal temp
response = r.urlopen(
    f'{url_global}')
data = response.read()


# Write data to file
filename = "./files/global_temp/global.txt"
file_ = open(filename, 'wb')
file_.write(data)

# Removes the last 12 lines
with open(r"./files/global_temp/global.txt", 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the last line
    # lines[:-1] from line 0 to the second last line
    fp.writelines(lines[:-13])

# Create a datafram
data = pd.read_csv(filename, delimiter="\s+", header=0)
# convert just columns "Year" and "Mo" to string
data[["Year", "Mo"]] = data[["Year", "Mo"]].astype(str)

#Connect to sql server
connect = sql.Database()
#Truncate table
connect.truncate_table('global')
#Insert Data
connect.InsertDf(data, 'global')
