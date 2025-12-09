# IMPORTS
import sklearn
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print( "All packages loaded successfully!" )
print( f"NumPy version: {np.__version__}" )
print( f"Pandas version: {pd.__version__}")
print( f"SciKit-Learn version: {sklearn.__version__}\N")

# generate synthetic two-dimensional data
X, y = make_blobs(random_state=1)

# build the clustering model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# predict the cluster for each data point
y_kmeans = kmeans.predict(X); print("Predicted cluster memberships:\n{}".format(y_kmeans))

# Each training data point in X is assigned a cluster label.
# You can find these labels in the kmeans.labels_ attribute:
print("Cluster memberships:\n{}".format(kmeans.labels_))

# visualize the clusters
plt.figure("KMeans Clustering Results")
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title('KMeans Clustering Results')

# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')

plt.show()
print("KMeans clustering completed and visualized successfully!")
