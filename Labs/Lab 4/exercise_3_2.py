import numpy as np
from prelab_fixed_point import fixedpt
from prelab_exercise_1 import order_of_convergence


def aitken_x(x, tol, n_max):
    p = [x[0]]
    for n in range(n_max):
        p.append(x[n] - (x[n+1] - x[n])**2 / (x[n] - 2*x[n+1] + x[n+2]))
        if abs(p[n] - p[n-1]) < tol:
            return np.array(p)
    raise Exception("Failed")


def g(x):
    return np.sqrt(10. / (x + 4))


pstar = 1.3652300134140976
p0 = 1.5
n_max = 100
tol = 1e-10

[p, x_all, ier] = fixedpt(g, p0, tol, n_max)
print(f"Fixed point method took {len(x_all)} iterations.")
aitken = aitken_x(x_all, tol, n_max)
print(f"Aitken method took {len(aitken)} iterations.")
order_fixed = order_of_convergence(pstar, x_all)
print(f"Fixed point method's order of convergence was {order_fixed}")
order_aitken = order_of_convergence(pstar, aitken)
print(f"Aitken's order of convergence was {order_aitken}.")
