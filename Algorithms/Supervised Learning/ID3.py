import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

data = {
    'Salary': ['High', 'High', 'Low', 'Low'],
    'Work Environment': ['Good', 'Bad', 'Good', 'Bad'],
    'Quit': ['Stay', 'Stay', 'Stay', 'Quit']
}
df = pd.DataFrame(data)
label_encoder = LabelEncoder()
df['Salary'] = label_encoder.fit_transform(df['Salary'])
df['Work Environment'] = label_encoder.fit_transform(df['Work Environment'])
df['Quit'] = label_encoder.fit_transform(df['Quit'])
X = df[['Salary', 'Work Environment']]
y = df['Quit']

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)



plt.figure(figsize=(8, 6))
plot_tree(model, feature_names=['Salary', 'Work Environment'], class_names=['Quit', 'Stay'], filled=True)
plt.title("Decision Tree Using ID3 Algorithm")
plt.show()
