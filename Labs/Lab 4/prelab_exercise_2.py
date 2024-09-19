import numpy as np

from prelab_fixed_point import fixedpt
from prelab_exercise_1 import order_of_convergence


def g(x):
    return np.sqrt(10. / (x + 4))


p0 = 1.5
n_max = 100
tol = 1e-10

[p, x_all, ier] = fixedpt(g, p0, tol, n_max)
print(f"2(a). It took {len(x_all[~np.isnan(x_all)])} iterations")

alpha = order_of_convergence(p, x_all)
print(f"2(b). The order of convergence is {alpha}")

error_const = abs(x_all[2] - p) / abs(x_all[1] - p) ** alpha
print(f"and the error constant is {error_const}.")
