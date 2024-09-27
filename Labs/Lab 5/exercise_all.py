import numpy as np
import time
from common_algorithms import bisection, newton, fixedpt

def bisection_basin(f, df, ddf, a, b, n_max=1000):
    def g(x):
        return 1 - (df(x)**2 - f(x) * ddf(x)) / df(x)**2

    if f(a) * f(b) > 0:
        raise Exception("a and b are the same sign")

    midpoint = []
    for i in range(n_max):
        midpoint.append((a + b) / 2.)
        if f(a) * f(midpoint[i]) > 0:
            a = midpoint[i]
        else:
            b = midpoint[i]
        if 0 < abs(g(midpoint[i])) < 1:
            return midpoint[i]
        print(midpoint[i])
    raise Exception("Number of iterations exceeded n_max")

def bi_newton(f, df, ddf, a, b, tol, n_max):
    midpoint = bisection_basin(f, df, ddf, a, b, n_max)
    return newton(f, df, midpoint, tol, n_max)

def f(x):
    return np.e ** (x**2 + 7*x - 30) - 1

def df(x):
    return (2*x + 7) * np.e ** (x**2 + 7*x - 30)

def ddf(x):
    return 2 * np.e ** (x**2 + 7*x - 30) + (2*x + 7)**2 * np.e ** (x**2 + 7*x - 30)


a = 2
b = 4.5
n_max = 1000
tol = 1e-10

t0 = time.perf_counter()
bi = bisection(f, a, b, tol, n_max)
t1 = time.perf_counter()
print(len(bi), t1-t0)

try:
    print(fixedpt(f, b, tol, n_max))
    print(len(fixedpt(f, b, tol, n_max)))
except OverflowError:
    print("Fixed point overflow error")

t0 = time.perf_counter()
ne = bi_newton(f, df, ddf, a, b, tol, n_max)
t1 = time.perf_counter()
print(len(ne), t1-t0)
