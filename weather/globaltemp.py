import pandas as pd


fileName = "./weather/files/global_temp.txt"

data = pd.read_csv(fileName, sep="\t", header=None)

print(data)
