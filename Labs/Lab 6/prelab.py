import numpy as np
from common_algorithms import order_of_convergence


def forward_dif(f, s, h):
    return (f(s + h) - f(s)) / h


def centered_dif(f, s, h):
    return (f(s + h) - f(s - h)) / (2. * h)


f = np.cos
s = np.pi / 2.
fps = -1.
h = 0.01 * 2. ** (-np.arange(0, 10))

fd = forward_dif(f, s, h)
fd_order = order_of_convergence(fps, fd)
cd = centered_dif(f, s, h)
cd_order = order_of_convergence(fps, cd)

print(f"Forward difference approximations: {fd}")
print(f"The order of convergence of the forward difference method is approximately {fd_order}\n")

print(f"Centered difference approximations: {cd}")
print(f"The order of convergence of the centered difference method is approximately {cd_order}")
