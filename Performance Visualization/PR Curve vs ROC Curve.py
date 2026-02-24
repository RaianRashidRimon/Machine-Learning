import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score

X, y = make_classification(n_samples=5000, weights=[0.95], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression().fit(X_train, y_train)
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
precision, recall, _ = precision_recall_curve(y_test, y_prob)
pr_auc = average_precision_score(y_test, y_prob)



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(fpr, tpr, label=f'ROC (AUC = {roc_auc:.3f})')
ax1.plot([0,1], [0,1], '--', color='gray')
ax1.set(xlabel='False Positive Rate', ylabel='True Positive Rate', title='ROC Curve')
ax1.legend(); ax1.grid(True, alpha=0.3)
ax2.plot(recall, precision, label=f'PR (AP = {pr_auc:.3f})')
ax2.plot([0,1], [y.mean(), y.mean()], '--', color='gray', label=f'Baseline ({y.mean():.3f})')
ax2.set(xlabel='Recall', ylabel='Precision', title='Precision-Recall Curve')
ax2.legend(); ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

