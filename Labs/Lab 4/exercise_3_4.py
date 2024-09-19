import numpy as np
from prelab_exercise_1 import order_of_convergence

"""
inputs:
f       - function
x       - start points
tol     - tolerance
n_max   - maximum number of iterations

output:
p       - array of iterations


Pseudocode:

def steffenson(f, x, tol, n_max):
    p = [x]
    for n in range(n_max):
        p.append(p[n] - (f(p[n]) - p[n])**2 / (f(f(p[n])) - 2*f(p[n]) + p[n]))
        if abs(p[n] - p[n+1]) < tol:
            return np.array(p)
    raise Exception("Failed")
"""


def steffenson(f, x, tol, n_max):
    p = [x]
    for n in range(n_max):
        p.append(p[n] - (f(p[n]) - p[n])**2 / (f(f(p[n])) - 2*f(p[n]) + p[n]))
        if abs(p[n] - p[n+1]) < tol:
            return np.array(p)
    raise Exception("Failed")


def g(x):
    return np.sqrt(10. / (x + 4))


pstar = 1.3652300134140976
p0 = 1.5
n_max = 100
tol = 1e-10

x_all = steffenson(g, p0, tol, n_max)
print(f"Steffenson method took {len(x_all)-1} iterations.")
order = order_of_convergence(pstar, x_all)
print(f"Steffenson's order of convergence was {order}.")
