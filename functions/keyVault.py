#import modules
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class KeyVault(object):
    def __init__(self, key_vault_name=None):
        '''
        This class uses azure credentials from the system.
        It contains methods for getting secrets and secret names as well as
        creating new secrets.

        :paran credentials: credential object containing the login credentials
        :param key_vault_name: name of the key vault
        '''
        self.credential = DefaultAzureCredential()
        self.keyVaultName = "kvjani"
        self.KVUri = "https://" + self.keyVaultName + ".vault.azure.net"
        self.client = SecretClient(
            vault_url=self.KVUri, credential=self.credential)

    def getSecret(self, secret_name: str, **kwargs) -> str:
        '''
        This method returns a secret's value. Requires a secret name

        :param secret_name: the name of the secret
        '''
        secret = self.client.get_secret(secret_name)
        return secret.value


KeyVault().getSecret("urlNve")