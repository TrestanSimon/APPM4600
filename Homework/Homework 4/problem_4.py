import numpy as np
from common_algorithms import fixedpt, newton


def order_of_convergence(p, phat):
    return (np.log(np.abs(phat[3] - p) / np.abs(phat[2] - p)) /
            np.log(np.abs(phat[2] - p) / np.abs(phat[1] - p)))


def newton_m(f, fp, fpp, p0, tol, n_max):
    def g(x):
        return x - f(x)*fp(x) / ((fp(x))**2 - f(x)*fpp(x))
    return fixedpt(g, p0, tol, n_max)

def newton_2c(f, fp, m, p0, tol, n_max):
    def g(x):
        return x - m * f(x) / fp(x)
    return fixedpt(g, p0, tol, n_max)


def f(x):
    return np.e**(3*x) - 27*x**6 + 27*x**4 * np.e**x - 9*x**2 * np.e**(2*x)

def fp(x):
    return 3*np.e**(3*x) - 162*x**5 + 108*x**3 * np.e**x + 27*x**4 * np.e**x - 18*x*np.e**(2*x) - 18*x**2 * np.e**(2*x)

def fpp(x):
    return 9*(np.e**x - 3*x**2)*(-x**2 * np.e**x + 30*x**2 - 8*x*np.e**x - 2*np.e**x + np.e**(2*x))

tol = 1e-20
p0 = 4
p = 3.7330807918830167

print(fpp(1))
n0 = newton(f, fp, p0, tol, n_max=1000)
n1 = newton_m(f, fp, fpp, p0, tol, n_max=1000)
n2 = newton_2c(f, fp, 3, p0, tol, n_max=1000)

print(order_of_convergence(p, n0))
print(len(n0))
print(order_of_convergence(p, n1))
print(len(n1))
print(order_of_convergence(p, n2))
print(len(n2))