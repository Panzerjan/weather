
# importing panda library
import pandas as pd

# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("./global_temp/file/global.txt")

# storing this dataframe in a csv file
dataframe1.to_csv('./global_temp/file/global.csv',
                  index=None)

fileName = './global_temp/file/global.csv'
data = pd.read_csv(fileName, sep='\s+',  header=None)
# TODO
# First row as Header

print(data)
