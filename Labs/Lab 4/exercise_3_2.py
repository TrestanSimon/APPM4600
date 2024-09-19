import numpy as np


def aitken_x(x, tol, n_max):
    p = [x[0]]
    for n in range(n_max):
        p.append(x[n] - (x[n+1] - x[n])**2 / (x[n] - 2*x[n+1] + x[n+2]))
        if abs(p[n] - p[n-1]) < tol:
            return np.array(p)
    raise Exception("Failed")
