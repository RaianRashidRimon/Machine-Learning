import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
precision = precision_score(y_test, y_pred)
recall    = recall_score(y_test, y_pred)
f1        = f1_score(y_test, y_pred)




metrics = ['Precision', 'Recall', 'F1-Score']
values  = [precision, recall, f1]




plt.figure(figsize=(7, 5))
plt.bar(metrics, values, color=['#4e79a7', '#f28e2b', '#76b7b2'])
plt.ylim(0, 1.05)
plt.ylabel('Score')
plt.title('Precision, Recall & F1-Score')
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(values):
    plt.text(i, v + 0.02, f'{v:.3f}', ha='center')
plt.show()
