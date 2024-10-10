import numpy as np


def vandermonde_coefficients(x, y):
    n = len(x)
    V = np.array([
        [x[j]**i for i in range(n)] for j in range(n)
    ])
    return np.linalg.solve(V, y)


def polynomial_from_coefficients(a, x):
    return np.array(np.sum([a[k] * x ** k for k in range(len(a))], axis=0))
