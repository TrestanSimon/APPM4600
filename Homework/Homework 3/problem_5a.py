import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x - 4. * np.sin(2. * x) - 3.


x_arr = np.linspace(-5, 10, 1000)

fig, ax = plt.subplots()
ax.plot(x_arr, f(x_arr))
ax.grid(lw=0.5, linestyle='--', c='k')
ax.axhline(0, lw=1, c='k')
ax.axvline(0, lw=1, c='k')
ax.set(xlabel='$x$', ylabel='$y$')

plt.savefig('problem_5a', dpi=300)
# plt.show()
