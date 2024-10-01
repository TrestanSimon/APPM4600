import numpy as np


def bisection(f, a, b, tol, n_max=1000):
    if f(a) * f(b) > 0:
        raise Exception("a and b are the same sign")

    midpoint = []
    for i in range(n_max):
        midpoint.append((a + b) / 2.)
        if f(a) * f(midpoint[i]) > 0:
            a = midpoint[i]
        else:
            b = midpoint[i]
        if abs(a - b) <= tol:
            return midpoint

    raise Exception("Number of iterations exceeded n_max")


def fixedpt(f, p0, tol, n_max):
    p = [p0]
    for i in range(n_max):
        p.append(f(p[i]))
        if abs(p[i+1] - p[i]) < tol:
            return p

    raise Exception("Number of iterations exceeded n_max")


def newton(f, df, p0, tol, n_max):
    def g(x):
        return x - f(x) / df(x)
    return fixedpt(g, p0, tol, n_max)


def order_of_convergence(p, phat):
    return (np.log(np.abs(phat[3] - p) / np.abs(phat[2] - p)) /
            np.log(np.abs(phat[2] - p) / np.abs(phat[1] - p)))
