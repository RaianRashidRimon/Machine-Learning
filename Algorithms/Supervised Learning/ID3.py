import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    'Salary': ['High', 'High', 'Low', 'Low'],
    'Work Environment': ['Good', 'Bad', 'Good', 'Bad'],
    'Quit': ['Stay', 'Stay', 'Stay', 'Quit']
}
df = pd.DataFrame(data)

# Encoding categorical variables
label_encoder = LabelEncoder()
df['Salary'] = label_encoder.fit_transform(df['Salary'])
df['Work Environment'] = label_encoder.fit_transform(df['Work Environment'])
df['Quit'] = label_encoder.fit_transform(df['Quit'])

# Print encoded dataset
#print("Encoded Dataset:")
#|print(df)

# Features and target
X = df[['Salary', 'Work Environment']]
y = df['Quit']

# Create Decision Tree classifier using ID3 algorithm
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# Plot the decision tree
plt.figure(figsize=(8, 6))
plot_tree(model, feature_names=['Salary', 'Work Environment'], class_names=['Quit', 'Stay'], filled=True)
plt.title("Decision Tree Using ID3 Algorithm")
plt.show()

