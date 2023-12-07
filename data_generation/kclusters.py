import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt

# Load your CSV data into a Pandas DataFrame
df = pd.read_csv("9x9.csv")

# Assuming X contains the features
X = df.drop(columns=['mode'])

# List for summed squared distances
sse = []

# Try a range of cluster numbers (let's say from 1 to 10)
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)

print(sse)

plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('k Number of Clusters')
plt.ylabel('Squared Distance Sums')
plt.title('Using the Elbow Method to find Optimal k')
plt.show()

kl = KneeLocator(range(1, 11), sse, curve='convex', direction='decreasing')
optimal_k = kl.elbow

print(f'Optimal number of clusters (k): {optimal_k}')