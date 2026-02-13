import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score

X, y = make_moons(n_samples=1200, noise=0.25, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5),
    n_estimators=100, #bagging with 100 trees
    max_samples=0.8,
    random_state=42,
    n_jobs=-1)

bagging.fit(X_train, y_train)
print("Bagging accuracy:         {:.3f}".format(
    accuracy_score(y_test, bagging.predict(X_test))
))

plt.figure(figsize=(9, 4))
plt.scatter(X_test[:, 0], X_test[:, 1], c=bagging.predict(X_test), cmap='coolwarm', s=40, alpha=0.7)
plt.title("Bagging (100 trees)")



plt.tight_layout()
plt.show()
