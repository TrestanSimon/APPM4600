import numpy as np
np.set_printoptions(precision=16)


def f(x):
    return x[0]**2 + 4.*x[1]**2 + 4.*x[2]**2 - 16.

def grad_f(x):
    return np.array([2.*x[0], 8.*x[1], 8.*x[2]])

def df(x):
    return np.array(f(x) * grad_f(x) / np.linalg.norm(grad_f(x))**2)

def iteration(df, x0, tol, n_max):
    x = [x0]
    for i in range(n_max):
        dx = df(x[i])
        x.append(x[i] - dx)
        if np.linalg.norm(np.abs(dx), np.inf) < tol:
            return np.array(x)
    raise Exception("Number of iterations exceeded n_max")


x0 = [1., 1., 1.]
tol = 1e-16

xn = iteration(df, x0, tol, 100)
x = xn[-1]

print(f"(x, y, z) = ({x[0]}, {x[1]}, {x[2]})")
# print(F(x))
print(f"found in {len(xn)} iterations.")

print(np.array([
    np.linalg.norm(xn[i+1]-x, np.inf) / np.linalg.norm(xn[i]-x, np.inf)**2
    for i in range(4)
]))
