import numpy as np
from bisection_code import bisection


def g(x):
    return 2.*x - 1. - np.sin(x)


approx, n_iter = bisection(g, 0., 1., 1e-8)
print(f"r = {approx} found in {n_iter} iterations.")
