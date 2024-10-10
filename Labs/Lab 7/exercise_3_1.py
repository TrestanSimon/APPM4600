import numpy as np
import matplotlib.pyplot as plt

from divided_differences import dd_table, eval_dd_polynomial
from lagrange import eval_lagrange
from vandermonde import vandermonde_coefficients, polynomial_from_coefficients


def f(x):
    return 1. / (1 + (10*x)**2)


def get_nodes(n):
    return np.array([-1 + (j - 1)*(2/(n-1)) for j in range(n+1)])


n = 32
nodes = get_nodes(n)
f_nodes = f(nodes)
x = np.linspace(-1, 1, 1000)
f_x = f(x)

vc = vandermonde_coefficients(nodes, f_nodes)
vc = polynomial_from_coefficients(vc, x)

la = eval_lagrange(x, nodes, f_nodes)

dd = dd_table(nodes, f_nodes)
dd = eval_dd_polynomial(x, nodes, dd)

fig, axs = plt.subplots(ncols=2)

axs[0].plot(x, vc, label='vc')
axs[0].plot(x, la, label='la')
axs[0].plot(x, dd, label='dd')
axs[0].plot(x, f_x, label='original')
axs[0].legend()

axs[1].plot(x, np.abs(vc - f_x), label='vc')
axs[1].plot(x, np.abs(la - f_x), label='la')
axs[1].plot(x, np.abs(dd - f_x), label='dd')
axs[1].legend()
axs[1].set(yscale='log')

plt.show()
