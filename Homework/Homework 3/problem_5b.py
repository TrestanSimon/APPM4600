import numpy as np


def x_np1(x_n):
    return - np.sin(2.*x_n) + 5.*x_n/4. - 3./4.


def fixedpt(x0, tol, n_max):
    count = 0
    while count < n_max:
        count = count + 1
        x1 = x_np1(x0)
        if abs(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier]
        x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]


def main():
    tol = 1e-16
    print(fixedpt(-0.9, tol, 100))
    print(fixedpt(-0.5, tol, 1000))
    print(fixedpt(1.73, tol, 1000))
    print(fixedpt(2, tol, 1000))
    print(fixedpt(4.53, tol, 100))


main()
