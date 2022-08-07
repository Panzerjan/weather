import os
import uuid
import sys
from azure.storage.filedatalake import DataLakeServiceClient
import configparser
from datetime import datetime


class lake():

    def storage_account_key():
        config = configparser.ConfigParser()
        config.read('./weather/config.ini')
        return config['lakekey']['key']

    def initialize_storage_account(storage_account_name, storage_account_key):

        try:
            global service_client

            service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
                "https", storage_account_name), credential=storage_account_key)

        except Exception as e:
            print(e)

    def list_directory_contents():
        try:

            file_system_client = service_client.get_file_system_client(
                file_system="weather")

            paths = file_system_client.get_paths(path="OpenW")

            for path in paths:
                print(path.name + '\n')

        except Exception as e:
            print(e)

    def upload_file(file_name, folder, local_file):
        try:

            file_system_client = service_client.get_file_system_client(
                file_system="weather")

            directory_client = file_system_client.get_directory_client(folder)

            file_client = directory_client.get_file_client(file_name)

            local_file = open(local_file, 'r')

            file_contents = local_file.read()

            file_client.upload_data(file_contents, overwrite=True)

        except Exception as e:
            print(e)


# Connect to lake
lake.initialize_storage_account('janistgac', lake.storage_account_key())

# List Content
lake.list_directory_contents()

now = datetime.now()
dato = now.strftime("%m-%d-%Y")
file_name = f"results-{dato}.csv"

lake.upload_file(f'sandnes.csv', 'OpenW',
                 f"./weather/files/sandnes.csv")
