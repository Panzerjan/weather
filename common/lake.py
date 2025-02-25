from azure.storage.filedatalake import DataLakeServiceClient
from azure.identity import ClientSecretCredential
from common.keyvault import secrets

class Lake:
    service_client = None  # Ensure it's properly initialized

    def __init__(self, path):
        self.path = path

    @staticmethod
    def initialize_storage_account(storage_account_name):
        try:
            # Authenticate using Service Principal
            credential = ClientSecretCredential(
                tenant_id=secrets.KeyVault().getSecret('internal-tenantid'),
                client_id=secrets.KeyVault().getSecret('Testsp'),
                client_secret=secrets.KeyVault().getSecret('TestSecret'),
            )

            Lake.service_client = DataLakeServiceClient(
                account_url=f"https://{storage_account_name}.dfs.core.windows.net",
                credential=credential
            )

            print("✅ Storage account initialized successfully.")

        except Exception as e:
            print(f"❌ Error initializing storage account: {e}")

    def list_directory_contents(self):
        try:
            if Lake.service_client is None:
                print("❌ Storage account is NOT initialized. Run initialize_storage_account() first.")
                return

            file_system_client = Lake.service_client.get_file_system_client(file_system="weather")
            paths = file_system_client.get_paths(self.path)

            for path in paths:
                print(path.name)

        except Exception as e:
            print(f"❌ Error listing directory contents: {e}")

    @staticmethod
    def upload_file(file_name, folder, local_file):
        try:
            if Lake.service_client is None:
                print("❌ Storage account is NOT initialized. Run initialize_storage_account() first.")
                return

            file_system_client = Lake.service_client.get_file_system_client(file_system="weather")
            directory_client = file_system_client.get_directory_client(folder)

            # ✅ Ensure the folder exists before uploading
            directory_client.create_directory()

            file_client = directory_client.get_file_client(file_name)

            with open(local_file, 'rb') as file:
                file_contents = file.read()

            file_client.upload_data(file_contents, overwrite=True)
            print(f"✅ File '{file_name}' uploaded successfully to '{folder}'.")

        except Exception as e:
            print(f"❌ Error uploading file: {e}")
