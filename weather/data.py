import pandas as pd

fileName = "./weather/files/sandnes.csv"

data = pd.read_csv(fileName, sep=",", header=None)

print(data)
