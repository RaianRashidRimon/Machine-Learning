import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

X, _ = make_blobs(
    n_samples=150,
    centers=4,
    cluster_std=1.7,
    random_state=8
)
model = AgglomerativeClustering(
    n_clusters=4,
    linkage='single',
    metric='euclidean'
)

labels = model.fit_predict(X)
plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=80, edgecolor='black')
plt.title("Hierarchical Clustering (Single Linkage)")
plt.show()
Z = linkage(X, method='single')



plt.figure(figsize=(11, 6))
dendrogram(Z, truncate_mode='level', p=5)
plt.title("Dendrogram (Single Linkage)")
plt.xlabel("Sample index")
plt.ylabel("Distance")
plt.show()
