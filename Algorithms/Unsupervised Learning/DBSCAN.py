import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

X, _ = make_moons(n_samples=750, noise=0.08, random_state=42)
X = StandardScaler().fit_transform(X)

db = DBSCAN(eps=0.3, min_samples=5).fit(X)

labels = db.labels_
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"Estimated number of clusters: {n_clusters}")
print(f"Estimated number of noise points: {n_noise}")

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=40, edgecolors='k', linewidth=0.4)
plt.title(f"DBSCAN result\n{len(set(labels))} components (including noise)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
