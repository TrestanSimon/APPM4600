import numpy as np


def xnp1(xn):
    return 12. / (1. + xn)


def order_of_convergence(p, phat):
    return (np.log(np.abs(phat[2] - p) / np.abs(phat[1] - p)) /
            np.log(np.abs(phat[1] - p) / np.abs(phat[0] - p)))


p = 3
x1 = p - 1e-10
x2 = xnp1(x1)
x3 = xnp1(x2)
x = [x1, x2, x3]

"""for i in range(100):
    xstar = xnp1(xstar)"""


print(order_of_convergence(p, x))
print(abs(x2 - p) / abs(x1 - p))
