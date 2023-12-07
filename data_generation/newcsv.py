import pandas as pd

source_csv = pd.read_csv('spotify-2023.csv')
destination_csv = pd.read_csv('9x9.csv')
columns_to_add = ["released_month"]
for i in columns_to_add:
    destination_csv[i] = source_csv[i]
destination_csv.to_csv('10x10.csv', index=False)