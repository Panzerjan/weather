from functions import keyVault


url = keyVault.KeyVault().getSecret('urlAir')

print(url)