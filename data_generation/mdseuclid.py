import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import pandas as pd


# Load your data from a CSV file into a NumPy array
data = np.loadtxt('8x8.csv', delimiter=',', skiprows=1)

# Calculate the Euclidean distance matrix
distance_matrix = pairwise_distances(data, metric='euclidean')

# Perform MDS to obtain the coordinates
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
coordinates = mds.fit_transform(distance_matrix)
output_file = 'mds_coordinates.csv'

# Save the coordinates to a CSV file
np.savetxt(output_file, coordinates, delimiter=',', header='X,Y', comments='')