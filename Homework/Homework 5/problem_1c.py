import numpy as np
np.set_printoptions(precision=16)


def newton_nd(F, J, x0, tol, n_max):
    x = [x0]
    for i in range(n_max):
        y = np.linalg.solve(J(x[i]), F(x[i]))
        x.append(x[i] - y)
        if np.linalg.norm(np.abs(y), np.inf) < tol:
            return np.array(x)
    raise Exception("Number of iterations exceeded n_max")


def F(x):
    return np.array([
        3. * x[0] ** 2 - x[1] ** 2,
        3. * x[0] * x[1] ** 2 - x[0] ** 3 - 1.
    ])


def J(x):
    return np.array([
        [6. * x[0], -2. * x[1]],
        [3. * x[1] ** 2 - 3. * x[0] ** 2, 6. * x[0] * x[1]]
    ])


p0 = [1, 1]
tol = 1e-16
fp = newton_nd(F, J, p0, tol, 100)

x = fp[-1]
print(f"(x, y) = ({x[0]}, {x[1]})")
# print(F(x))
print(f"found in {len(fp)} iterations.")
