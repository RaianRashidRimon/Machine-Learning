import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


temperatures = np.array([14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]).reshape(-1, 1)
sales = np.array([215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408])



model = LinearRegression()
model.fit(temperatures, sales)
temp_range = np.linspace(min(temperatures), max(temperatures), 100).reshape(-1, 1)
sales_pred = model.predict(temp_range)
plt.figure(figsize=(10, 6))
plt.scatter(temperatures, sales, color='blue', label='Data Points')
plt.plot(temp_range, sales_pred, color='red', label='Best-Fit Line')
plt.title('Ice Cream Sales vs. Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()




print(f'Best-Fit Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}')
