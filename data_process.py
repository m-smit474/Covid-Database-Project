import pandas as pd

# read in files

dir = input("Enter file path: ")

data = pd.read_csv(dir)

print(data.head())