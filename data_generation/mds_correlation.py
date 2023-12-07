import numpy as np
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances


data = np.loadtxt('8x8.csv', delimiter=',', skiprows=1)

# Step 1: Calculate 1-|correlation| distance matrix
correlation_matrix = np.corrcoef(data.T)
distance_matrix = 1 - np.abs(correlation_matrix)

# Step 2: Perform MDS
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=0)
coordinates = mds.fit_transform(distance_matrix)

output_file = 'mdscorrelation_coordinates.csv'

# Save the coordinates to a CSV file
np.savetxt(output_file, coordinates, delimiter=',', header='X,Y', comments='')