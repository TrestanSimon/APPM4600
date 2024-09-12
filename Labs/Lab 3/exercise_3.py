import numpy as np
from modified_fixedpt_example import fixedpt

x0 = 1.
tol = 1e-10
n_max = 1000

f = lambda x: x ** 2 * (x - 1)

functions = {
    "a": lambda x: x * (1. + (7. - x**5)/(x**2))**3,
    "b": lambda x: x - (x**5 - 7.) / (x**2),
    "c": lambda x: x - (x**5 - 7.) / (5. * x**4),
    "d": lambda x: x - (x**5 - 7.) / 12.,
}


for letter, f in functions.items():
    try:
        [astar, ier] = fixedpt(f, x0, tol, n_max)
        print("\nFor problem", letter)
        print('the approximate root is', astar)
        print('the error message reads:', ier)
        print('f(astar) =', f(astar))
    except OverflowError:
        print(f"\n{letter} did not converge.")

print("\n7^(1/5) = ", 7.**(1/5.))


"""
The algorithm converges for functions (c) and (d), but it does not converge for functions (a) and (b).
For (a) and (b), the algorithm does not converge since f(1) is not within the basin of convergence resulting in
successive iterations getting farther and farther from the fixed point, eventually raising an Overflow error.
For (c) and (d), the algorithm does converge since f(1) is within the basin of convergence.
"""
