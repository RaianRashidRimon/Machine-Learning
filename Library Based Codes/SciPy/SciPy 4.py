from scipy.optimize import fsolve

def func(x):
    return x**2 - 4

root = fsolve(func, x0=1)
print("Root:", root)
