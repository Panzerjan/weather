from datetime import datetime
from azure.storage.filedatalake import DataLakeServiceClient
import configparser
import os
import shutil

class files():

    def set_filename(self, file_name , file_struc):
        '''
         Input:
            file_name: str --> name of the file
            file_struc: str --> extension file etc ,json, xml, csv
        '''
        now = datetime.now()
        dato = now.strftime("%m-%d-%Y")
        file = file_name
        return f"{file}_{dato}.{file_struc}"

    def move_file(new_path, his_path , file):
            shutil.move(f"{new_path}{file}", his_path)
            print(f'Moved {file} from {new_path} to {his_path}')

class lake():

    def __init__(self, path):
        self.path = path


    def storage_account_key():
        config = configparser.ConfigParser()
        config.read('./functions/config.ini')
        return config['lakekey']['key']


    def initialize_storage_account(storage_account_name, storage_account_key):

        try:
            global service_client

            service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
                "https", storage_account_name), credential=storage_account_key)

        except Exception as e:
            print(e)

    def list_directory_contents(self):
        try:

            file_system_client = service_client.get_file_system_client(
                file_system="weather")

            paths = file_system_client.get_paths(self.path)

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