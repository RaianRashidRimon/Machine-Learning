import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) + np.random.normal(0, 4, 11)
plt.scatter(X, y, color='blue', label='Data points')



poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)


X_range = np.linspace(0, 10, 200).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = model.predict(X_range_poly)



plt.plot(X_range, y_range_pred, color='red', linewidth=2, label='Polynomial fit (degree 2)')
plt.title("Polynomial Regression Example")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("R² score:", round(r2_score(y, y_pred), 4))
