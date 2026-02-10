import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(n_samples=1200, centers=5, cluster_std=1.4, random_state=42)
X = StandardScaler().fit_transform(X)


ms = MeanShift(bandwidth=None, bin_seeding=True).fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
n_clusters = len(np.unique(labels))


print(f"Number of clusters {n_clusters}")
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, edgecolors='white', linewidth=0.6)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=200, linewidths=3, label='Centers')
plt.title("Mean Shift Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

