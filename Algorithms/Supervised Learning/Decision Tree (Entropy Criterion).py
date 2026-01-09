import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
class_names = iris.target_names


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# using criterion='entropy' for ID3-like behavior, or 'gini' for CART
dt = DecisionTreeClassifier(
    criterion='entropy',        # ID3/C4.5 use entropy (Information Gain)
    max_depth=3,         
    min_samples_split=2,     
    random_state=42
)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")


plt.figure(figsize=(20, 10))  
plot_tree(
    dt, 
    feature_names=feature_names, 
    class_names=class_names, 
    filled=True, 
    rounded=True, 
    fontsize=12
)
plt.title("Decision Tree (Entropy Criterion, ID3/C4.5-like)", fontsize=16)
plt.show()
