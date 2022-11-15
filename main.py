from common.server import sql
import pyodbc
import pandas as pd

from  common.keyvault.secrets import KeyVault

data = pd.read_csv('./files/global_temp/global.txt', delimiter="\s+", header=0)
# convert just columns "a" and "b"
data[["Year", "Mo"]] = data[["Year", "Mo"]].astype(str)
print(data)
print(data.dtypes)
# data.apply(pd.to_numeric) # convert all columns of DataFrame
columns = list(data.keys())


test = sql.Database()
test.truncate_table('global')
test.InsertDf(data, 'global')

#file2 = './files/nve/his_files/HentOffentligDataSisteUke_2022-11-10.json'

#test.InsertJsonData(file2)

# import glob
# import os.path

# folder_path = r'./files/nve/his_files/'
# file_type = r'\*type'
# files = glob.glob(folder_path + file_type)
# max_file = max(files, key=os.path.getctime)

# print(max_file)