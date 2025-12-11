import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

X = np.array([[2, 1], [1, 2], [3, 1], [1, 3]])  
y = np.array([1, -1, 1, -1])

model = SVC(kernel='linear')
model.fit(X, y)
w = model.coef_[0]
b = model.intercept_[0]


plt.figure(figsize=(10, 7))
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', marker='o', 
            s=100, label='Positive Class (+1)')
plt.scatter(X[y == -1][:, 0], X[y == -1][:, 1], color='red', marker='x', 
            s=100, label='Negative Class (-1)')


x_values = np.linspace(0, 4, 100)
y_values = -(w[0] / w[1]) * x_values - (b / w[1])
plt.plot(x_values, y_values, 'k-', lw=2, label='Decision Boundary')
margin = 1 / np.sqrt(np.sum(w**2))
y_pos_margin = -(w[0] / w[1]) * x_values - (b - 1) / w[1]
y_neg_margin = -(w[0] / w[1]) * x_values - (b + 1) / w[1]
plt.plot(x_values, y_pos_margin, 'k--', lw=1)
plt.plot(x_values, y_neg_margin, 'k--', lw=1)



support_vectors = model.support_vectors_
plt.scatter(support_vectors[:, 0], support_vectors[:, 1], s=150, 
            facecolors='none', edgecolors='green', linewidths=2, 
            label='Support Vectors')
equation = f"Hyperplane: {w[0]:.2f}x + {w[1]:.2f}y + {b:.2f} = 0"
plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', alpha=0.8))
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Simple SVM Classification with Hyperplane')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xlim(0, 4)
plt.ylim(0, 4)

plt.tight_layout()
plt.show()



new_point = np.array([[2.5, 2]])
prediction = model.predict(new_point)
predicted_label = 'Positive' if prediction[0] == 1 else 'Negative'
print(f"Prediction for new point [2.5, 2]: {predicted_label}")
