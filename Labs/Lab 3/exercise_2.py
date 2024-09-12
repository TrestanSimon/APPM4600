import numpy as np
from modified_bisection_example import bisection


tol = 1e-5

f = lambda x: x ** 2 * (x - 1)

points = {
    "a": (0., 2.4, lambda x: (x - 1) * (x - 3) * (x - 5)),
    "b": (0., 2., lambda x: (x - 1) ** 2 * (x - 3)),
    "c": (0., 0.1, lambda x: np.sin(x)),
    "c2:": (0.5, 3. * np.pi / 4., lambda x: np.sin(x)),
}

for letter, p in points.items():
    [astar, ier] = bisection(p[2], p[0], p[1], tol)
    print("\nFor problem", letter)
    print('the approximate root is', astar)
    print('the error message reads:', ier)
    print('f(astar) =', f(astar))


"""
The algorithm behaved as I expected.

The algorithm succeeded when the provided initial x values resulted in one f(x) being positive and the other being negative (e.g., (a))
or when one or both f(x) was zero (e.g., (c))

When the algorithm succeeded (i.e., for (a) and (c)), the expected accuracy was achieved.
"""
