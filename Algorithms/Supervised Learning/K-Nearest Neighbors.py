import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Smaller dataset
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [2.5, 1.5]])
y = np.array([0, 0, 1, 1, 0])

# Train KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)  # k=3
knn.fit(X, y)

# Predict on a test point
test_point = np.array([[2.5, 2.5]])
prediction = knn.predict(test_point)
print(f"Prediction for {test_point[0]}: Class {prediction[0]}")

# Accuracy on training data (small dataset, no split)
y_pred = knn.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Training Accuracy: {accuracy:.2f}")

# Visualization
def plot_knn_boundary(X, y, knn, test_point, prediction, title):
    plt.figure(figsize=(8, 6))
    
    # Scatter plot of training data points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', s=100, edgecolors='k', label='Training Data')
    
    # Create mesh grid for decision boundary
    h = 0.02  # Step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    # Predict over the grid
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundary
    plt.contourf(xx, yy, Z, cmap='bwr', alpha=0.2)
    plt.contour(xx, yy, Z, colors='k', levels=[0], linestyles=['-'])
    
    # Plot test point
    plt.scatter(test_point[:, 0], test_point[:, 1], c='green', s=150, marker='*', 
                label=f'Test Point (Class {prediction[0]})')
    
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Visualize
plot_knn_boundary(X, y, knn, test_point, prediction, "KNN Decision Boundary (k=3)")
