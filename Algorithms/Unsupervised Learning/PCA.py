
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()

X = iris.data          
y = iris.target 
feature_names = iris.feature_names

print("Original shape:", X.shape)       
print("Features:", feature_names)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
explained_variance = pca.explained_variance_ratio_ * 100

print("\nResults:")
print(f"PC1 explains {explained_variance[0]:.1f}% of the variance")
print(f"PC2 explains {explained_variance[1]:.1f}% of the variance")
print(f"Together they explain {sum(explained_variance):.1f}%")
print("New shape after PCA:", X_pca.shape)

plt.figure(figsize=(9, 7))
colors = ['#e74c3c', '#3498db', '#2ecc71']
labels = ['Setosa', 'Versicolor', 'Virginica']

for i in range(3):
    plt.scatter(X_pca[y == i, 0], 
                X_pca[y == i, 1],
                c=colors[i], 
                label=labels[i],
                edgecolor='white',
                s=80,
                alpha=0.9)

plt.title("Iris dataset in 2D after PCA", fontsize=14, pad=15)
plt.xlabel(f"Principal Component 1 ({explained_variance[0]:.1f}% variance)", fontsize=12)
plt.ylabel(f"Principal Component 2 ({explained_variance[1]:.1f}% variance)", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
