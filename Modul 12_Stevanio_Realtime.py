import pandas as pd

file_path = 'C:/Users/Stevanio/Downloads/Negara.csv'

data = pd.read_csv(file_path)

print("Data Awal:")
print(data.head())

print("\nNama Kolom:")
print(data.columns)
