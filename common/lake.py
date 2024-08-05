
from azure.storage.filedatalake import DataLakeServiceClient
from common.keyvault import secrets

class lake():

    def __init__(self, path):
        self.path = path

    def storage_account_key():
        key =secrets.KeyVault().getSecret('lakekey')
        return key

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