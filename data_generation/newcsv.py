import pandas as pd

source_csv = pd.read_csv('9x9.csv')
destination_csv = pd.read_csv('mds_coordinates.csv')
columns_to_add = ["released_day","bpm","danceability_%","valence_%","energy_%","acousticness_%","liveness_%","speechiness_%"]
for i in columns_to_add:
    destination_csv[i] = source_csv[i]
destination_csv.to_csv('mds_coordinates.csv', index=False)