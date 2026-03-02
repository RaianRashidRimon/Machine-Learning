from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=1000, n_features=12, random_state=42)
model = RandomForestClassifier(random_state=42).fit(X, y)
importances = model.feature_importances_


plt.bar(range(len(importances)), importances)
plt.xlabel('Feature Index')
plt.ylabel('Importance')
plt.title('Feature Importance (Random Forest)')
plt.show()
