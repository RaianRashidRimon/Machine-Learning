import numpy as np
import matplotlib.pyplot as plt

def fuzzy_c_means(X, c, m=2.0, max_iter=100, error=0.005):
    n, d = X.shape
    U = np.random.dirichlet(np.ones(c), size=n)
    
    for _ in range(max_iter):
        U_old = U.copy()
        Um = U ** m
        centers = (Um.T @ X) / Um.sum(axis=0)[:, np.newaxis]
        diff = X[:, np.newaxis, :] - centers[np.newaxis, :, :]
        dist = np.sum(diff ** 2, axis=2) + 1e-12
        tmp = dist ** (-1 / (m - 1))
        U = tmp / tmp.sum(axis=1, keepdims=True)
        if np.max(np.abs(U - U_old)) < error:
            break
    labels = np.argmax(U, axis=1)
    return U, centers, labels

np.random.seed(42)
X1 = np.random.normal([1, 2], 0.5, (150, 2))
X2 = np.random.normal([4, 5], 0.7, (120, 2))
X3 = np.random.normal([6, 1], 0.6, (130, 2))
X = np.vstack([X1, X2, X3])
U, centers, labels = fuzzy_c_means(X, c=3)


plt.figure(figsize=(7, 5))
plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis', s=40, alpha=0.7)
plt.scatter(centers[:,0], centers[:,1], c='red', marker='X', s=300, edgecolor='black', linewidth=2)
plt.title("Fuzzy C-Means")
plt.grid(True, alpha=0.3)
plt.show()
