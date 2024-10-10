import numpy as np
import matplotlib.pyplot as plt

from lagrange import eval_lagrange


def f(x):
    return 1. / (1 + (10*x)**2)


def get_nodes(n):
    return np.array([
        np.cos((2.*j - 1.) * np.pi / (2.*n))
        for j in range(1, n+1)
    ])


n = 31
nodes = get_nodes(n)
f_nodes = f(nodes)
x = np.linspace(-1, 1, 1000)
f_x = f(x)

la = eval_lagrange(x, nodes, f_nodes)

fig, axs = plt.subplots(ncols=2)

axs[0].plot(x, la, label='la')
axs[0].plot(x, f_x, label='original')
axs[0].legend()

axs[1].plot(x, np.abs(la - f_x), label='la')
axs[1].legend()
axs[1].set(yscale='log')

plt.show()
