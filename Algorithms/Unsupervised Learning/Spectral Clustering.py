import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_moons, make_circles

X, _ = make_circles(n_samples=500, noise=0.06, factor=0.4, random_state=42)
plt.figure(figsize=(9, 4))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], s=40, c='gray', edgecolor='k', alpha=0.7)
plt.title("Original data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

clustering = SpectralClustering(
    n_clusters=2,
    affinity='rbf',
    gamma=30,
    random_state=42
)
labels = clustering.fit_predict(X)
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], s=40, c=labels, cmap='viridis', edgecolor='k', alpha=0.7)
plt.title("Spectral Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.tight_layout()
plt.show()


