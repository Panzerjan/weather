import urllib.request as r
import sys

sys.path.append( './functions/' )
from keyVault import KeyVault

# set variables
url_global= KeyVault().getSecret('urlGobalTemp')

# Read the date from Gobal temp
response = r.urlopen(
    f'{url_global}')
data = response.read()


# Write data to file
filename = "./global_temp/file/global.txt"
file_ = open(filename, 'wb')
file_.write(data)

# Removes the last 12 lines
with open(r"./global_temp/file/global.txt", 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the last line
    # lines[:-1] from line 0 to the second last line
    fp.writelines(lines[:-12])

