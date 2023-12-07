import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the CSV file
df = pd.read_csv("9x9.csv")

# Separate the features (X) from the target variable (mode)
X = df.drop(columns=['mode'])

# Standardize the features by removing the mean and scaling to unit variance
X_std = StandardScaler().fit_transform(X)

# Apply PCA with two components
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_std)

# Create a DataFrame with the principal components
pca_df = pd.DataFrame(data=principal_components, columns=['PCA1', 'PCA2'])

# Concatenate the principal components DataFrame with the target variable (mode)
result_df = pd.concat([pca_df, df['mode']], axis=1)

# Compute loading vectors in order to display on biplot!
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'])

# print(loadings)
# Save the result to a new CSV file
result_df.to_csv("pca_result.csv", index=False)