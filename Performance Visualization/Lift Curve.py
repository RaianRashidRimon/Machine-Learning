import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=4000, weights=[0.92], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
proba = LogisticRegression().fit(X_train, y_train).predict_proba(X_test)[:, 1]
order = np.argsort(proba)[::-1]
y_sorted = y_test[order]
cumi_true = np.cumsum(y_sorted)
lift = cumi_true / (np.arange(1, len(cumi_true)+1) * cumi_true[-1] / len(cumi_true))




plt.plot(np.linspace(0, 100, len(lift)), lift)
plt.plot([0, 100], [1, 1], '--', color='gray')
plt.xlabel('% of population')
plt.ylabel('Lift')
plt.title('Lift Curve')
plt.grid(True, alpha=0.3)
plt.show()
