import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

#pca
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
explained_variance = pca.explained_variance_ratio_ * 100

print("\nPCA Results:")
print(f"PC1 explains {explained_variance[0]:.1f}% of the variance")
print(f"PC2 explains {explained_variance[1]:.1f}% of the variance")
print(f"Together they explain {sum(explained_variance):.1f}%")
print("New shape after PCA:", X_pca.shape)

colors = ['#e74c3c', '#3498db', '#2ecc71']
labels = ['Setosa', 'Versicolor', 'Virginica']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

#after pca
for i in range(3):
    ax1.scatter(X_pca[y == i, 0], X_pca[y == i, 1],
                c=colors[i], label=labels[i],
                edgecolor='white', s=80, alpha=0.9)
ax1.set_title("After PCA (PC1 vs PC2)", fontsize=13, pad=10)
ax1.set_xlabel(f"Principal Component 1 ({explained_variance[0]:.1f}% variance)", fontsize=11)
ax1.set_ylabel(f"Principal Component 2 ({explained_variance[1]:.1f}% variance)", fontsize=11)
ax1.legend()
ax1.grid(True, alpha=0.3)

#before pca
for i in range(3):
    ax2.scatter(X[y == i, 2], X[y == i, 3],
                c=colors[i], label=labels[i],
                edgecolor='white', s=80, alpha=0.9)
ax2.set_title("Before PCA – Petal Length vs Petal Width", fontsize=13, pad=10)
ax2.set_xlabel("Petal Length (cm)", fontsize=11)
ax2.set_ylabel("Petal Width (cm)", fontsize=11)
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle("Iris Dataset: Before vs After PCA", fontsize=15, y=1.02)
plt.tight_layout()
plt.show()
df = pd.DataFrame(X, columns=feature_names)
df['species'] = pd.Categorical.from_codes(y, labels)
sns.pairplot(df, hue='species',
             palette=colors,
             markers='o',
             diag_kind='hist',
             plot_kws={'s': 60, 'alpha': 0.9, 'edgecolor': 'white'})
plt.suptitle("Iris Dataset – All Features (Original Scale)", y=1.02, fontsize=15)
plt.show()
