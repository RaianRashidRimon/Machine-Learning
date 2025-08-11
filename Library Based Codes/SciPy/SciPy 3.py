import numpy as np
from scipy.linalg import solve

A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6])
x = solve(A, b)
print("Solution:", x)
