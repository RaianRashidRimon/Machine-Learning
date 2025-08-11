from scipy.integrate import quad

def func(x):
    return x**2

integral, _ = quad(func, 0, 2)
print("Integral:", integral)
