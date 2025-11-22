import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs




X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X)
centers = kmeans.cluster_centers_
labels = kmeans.labels_





plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
