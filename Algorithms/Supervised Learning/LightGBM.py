import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import lightgbm as lgb

X, y = make_classification(
    n_samples=2000,
    n_features=10,
    n_informative=6,
    n_redundant=2,
    random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

params = {
    'objective': 'binary',       
    'metric': 'binary_logloss',   
    'learning_rate': 0.1,
    'max_depth': 5,
    'num_leaves': 31,
    'verbose': -1  }

model = lgb.train(
    params,
    train_data,
    num_boost_round=100,
    valid_sets=[test_data],
    valid_names=['validation'])
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob >= 0.5).astype(int)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")


lgb.plot_importance(model, max_num_features=10, figsize=(8, 5))
plt.title("Feature importance")
plt.grid(False)
plt.show()
