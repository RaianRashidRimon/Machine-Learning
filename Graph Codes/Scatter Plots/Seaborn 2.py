import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

countries = ['Madagascar', 'India', 'Mexico', 'Taiwan', 'Norway']
production = np.array([800, 3100, 9600, 25300, 40000])
birth_rate = np.array([5.70, 2.85, 2.49, 1.57, 1.78])
model = LinearRegression()
model.fit(production.reshape(-1, 1), birth_rate)
prod_range = np.linspace(min(production), max(production), 100)
birth_pred = model.predict(prod_range.reshape(-1, 1))



plt.figure(figsize=(10, 6))
sns.scatterplot(x=production, y=birth_rate, color='blue', s=100)
for i, country in enumerate(countries):
    plt.annotate(country, (production[i], birth_rate[i]), xytext=(5, 5), 
                 textcoords='offset points', fontsize=8)
plt.plot(prod_range, birth_pred, color='red', label='Best-Fit Line')
plt.title('Yearly Production per Person vs. Birth Rate by Country')
plt.xlabel('Yearly Production per Person ($)')
plt.ylabel('Birth Rate (per woman)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

print(f'Best-Fit Line: y = {model.coef_[0]:.4f}x + {model.intercept_:.4f}')
