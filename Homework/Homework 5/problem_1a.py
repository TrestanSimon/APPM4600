import numpy as np


def fixedpt_nd(F, M, p0, tol, n_max):
    p = [np.array(p0)[:, np.newaxis]]
    for i in range(n_max):
        p_n = p[i] - M @ np.array([f(np.squeeze(p[i])) for f in F])[:, np.newaxis]
        p.append(p_n)
        if np.amax(np.abs(p[i+1].T - p[i].T)) < tol:
            return p
    raise Exception("Number of iterations exceeded n_max")


def f(x):
    return 3.*x[0]**2 - x[1]**2

def g(x):
    return 3.*x[0]*x[1]**2 - x[0]**3 - 1.


p0 = [1, 1]
M = [
    [1/6., 1/18.],
    [0., 1/6.]
]
tol = 1e-16
fp = fixedpt_nd([f, g], M, p0, tol, 100)

p = np.squeeze(fp[-1])
print(p)
print(f(p), g(p))
