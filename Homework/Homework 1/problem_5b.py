import numpy as np
import matplotlib.pyplot as plt


def f(x, delta):
    return np.cos(x + delta) - np.cos(x)


def g(x, delta):
    return -2. * np.sin(x + delta / 2.) * np.sin(delta / 2.)


delta_arr = 10. ** np.array(range(-16, 1))

fig, ax = plt.subplots(layout="tight")
ax.scatter(delta_arr, np.abs(g(np.pi, delta_arr) - f(np.pi, delta_arr)), label="$x=\\pi$")
ax.scatter(delta_arr, np.abs(g(1e6, delta_arr) - f(1e6, delta_arr)), label="$x=10^6$")

ax.set(xscale='log', yscale='log', xlabel="$\\delta$", ylabel="$|\\cos(x+\\delta) - \\cos(x) - f(x,\\delta)|$")
ax.grid()
ax.legend()
plt.savefig("problem_5b.png", dpi=300)
# plt.show()
