import numpy as np
from bisection_code import bisection


def f(x):
    return x**3 + x - 4.


a = 1.
b = 4.
tol = 1e-3

print(bisection(f, a, b, tol, 12))
