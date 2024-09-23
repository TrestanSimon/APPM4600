import numpy as np
from bisection_code import bisection


def f(x):
    return (x - 5.)**9


def g(x):
    return -1953125 + 3515625*x - 2812500*x**2 + 1312500*x**3 - 393750*x**4 + 78750*x**5 - 10500*x**6 + 900*x**7 - 45*x**8 + x**9


a = 4.82
b = 5.2
tol = 1e-4


print(bisection(f, a, b, tol))
print(bisection(g, a, b, tol))

print(f(5.01))
print(g(5.01))
