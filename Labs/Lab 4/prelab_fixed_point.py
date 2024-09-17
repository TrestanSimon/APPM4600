import numpy as np


def driver():
    # test functions
    f1 = lambda x: 1 + 0.5 * np.sin(x)
    # fixed point is alpha1 = 1.4987....

    f2 = lambda x: 3 + 2 * np.sin(x)
    # fixed point is alpha2 = 3.09...

    n_max = 100
    tol = 1e-6

    # test f1 '''
    x0 = 0.0
    [xstar, ier] = fixedpt(f1, x0, tol, n_max)
    print('the approximate fixed point is:', xstar)
    print('f1(xstar):', f1(xstar))
    print('Error message reads:', ier)

    # test f2 '''
    x0 = 0.0
    [xstar, ier] = fixedpt(f2, x0, tol, n_max)
    print('the approximate fixed point is:', xstar)
    print('f2(xstar):', f2(xstar))
    print('Error message reads:', ier)


def fixedpt(f, x0, tol, n_max):
    """
    x0 = initial guess
    n_max = max number of iterations
    tol = stopping tolerance
    """

    all_x = np.ones((n_max, 1)) * np.nan

    i = 0
    while i < n_max:
        x1 = f(x0)
        all_x[[i]] = x1
        i += 1
        if abs(x1 - x0) < tol:
            ier = 0
            return all_x, ier
        x0 = x1

    ier = 1
    return all_x, ier


# driver()
