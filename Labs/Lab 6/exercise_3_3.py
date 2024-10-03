import numpy as np
np.set_printoptions(precision=10)


def slacker_newton_fd(F, x0, h, tol, n_max):
    x = [x0]
    for i in range(n_max):
        J = np.linalg.inv(fd_J(F, x[i], h))
        print(J)
        dx = np.linalg.solve(J, F(x[i]))
        x.append(x[i] - dx)
        if np.linalg.norm(np.abs(dx), np.inf) < tol:
            return np.array(x)
    print(x)
    raise Exception("Number of iterations exceeded n_max")


def forward_dif(f, s, h):
    return (f(s + h) - f(s)) / np.linalg.norm(h, np.inf)


def F(x):
    return np.array([
        4.*x[0]**2 + x[1]**2 - 4.,
        x[0] + x[1] - np.sin(x[0] - x[1])
    ])


def fd_J(F, x, h):
    fx = forward_dif(F, x, np.array([h, 0.]))
    fy = forward_dif(F, x, np.array([0., h]))
    return np.array([
        fx, fy
    ]).T


x0 = [1., 0.]
h = 1.e-7
tol = 1e-10
fp = slacker_newton_fd(F, x0, h, tol, 100)

x = fp[-1]
print(f"(x, y) = ({x[0]}, {x[1]})")
print(F(x))
print(f"found in {len(fp)} iterations.")
