import matplotlib.pyplot as plt
import numpy as np

from vandermonde import vandermonde_coefficients, polynomial_from_coefficients
from lagrange import eval_lagrange
from divided_differences import dd_table, eval_dd_polynomial


def f(x):
    return np.sin(x)


nodes = np.linspace(0, np.pi, 10)
x = np.linspace(0, 2.*np.pi, 20)
f_nodes = f(nodes)

vc = vandermonde_coefficients(nodes, f_nodes)
vc = polynomial_from_coefficients(vc, x)

la = eval_lagrange(x, nodes, f_nodes)

dd = dd_table(nodes, f_nodes)
dd = eval_dd_polynomial(x, nodes, dd)


fig, ax = plt.subplots()

ax.plot(x, vc, label='vc')
ax.plot(x, la, label='la')
ax.plot(x, dd, label='dd')
ax.legend()
plt.show()
