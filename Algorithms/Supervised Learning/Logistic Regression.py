import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample Data: Hours Studied vs Pass/Fail (1 = Pass, 0 = Fail)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Independent variable
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # Dependent variable (Binary: 0 = Fail, 1 = Pass)

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and Train the Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # Probability of class 1

# Model Performance Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print Results
print(f"Model Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(report)

# Plot the Sigmoid Curve
X_range = np.linspace(0, 12, 100).reshape(-1, 1)
y_prob_curve = model.predict_proba(X_range)[:, 1]

plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X_range, y_prob_curve, color='red', linestyle="--", label="Sigmoid Curve")
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression: Hours Studied vs Pass/Fail")
plt.legend()
plt.show()
