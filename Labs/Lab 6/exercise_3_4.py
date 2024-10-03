import numpy as np
np.set_printoptions(precision=10)


def hybrid_slacker_newton(F, J, x0, tol, n_max):
    x = [x0]
    for i in range(n_max):
        if i % 4 == 0:
            J_inv = np.linalg.inv(J(x[i]))
        dx = J_inv @ F(x[i])
        x.append(x[i] - dx)
        if np.linalg.norm(np.abs(dx), np.inf) < tol:
            return np.array(x)
    raise Exception("Number of iterations exceeded n_max")


def F(x):
    return np.array([
        4.*x[0]**2 + x[1]**2 - 4.,
        x[0] + x[1] - np.sin(x[0] - x[1])
    ])


def J(x):
    return np.array([
        [8.*x[0], 2.*x[1]],
        [1 - np.cos(x[0] - x[1]), 1 + np.cos(x[0] - x[1])]
    ])


x0 = [1., 0.]
tol = 1e-10
fp = hybrid_slacker_newton(F, J, x0, tol, 100)

x = fp[-1]
print(f"(x, y) = ({x[0]}, {x[1]})")
print(F(x))
print(f"found in {len(fp)} iterations.")
