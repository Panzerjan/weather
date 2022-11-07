from functions import keyVault
import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = keyVault.KeyVault().getSecret('SqlServer')
database = keyVault.KeyVault().getSecret('Sqldb')
username = keyVault.KeyVault().getSecret('Sqladmin')
password = keyVault.KeyVault().getSecret('SqlPwd')
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

df = pd.read_json('./files/nve/his_files/HentOffentligDataSisteUke_2022-11-05.json')


for row in df.itertuples():
    cursor.execute('''
                INSERT INTO vannmagasin(dato_id , omrType, omrnr, iso_aar, iso_uke, fyllingsgrad,kapasitet_TWh,fylling_TWh,neste_Publiseringsdato,fyllingsgrad_forrige_uke,endring_fyllingsgrad)
                VALUES (?,?,?,?,?,?)
                ''',
                row.dato_id,
                row.omrType,
                row.omrnr,
                row.iso_aar,
                row.iso_uke,
                row.fyllingsgrad,
                row.kapasitet_TWh,
                row.fylling_TWh,
                row.neste_Publiseringsdato,
                row.fyllingsgrad_forrige_uke,
                row.endring_fyllingsgrad
                )
cnxn.commit()