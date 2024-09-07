import numpy as np
import matplotlib.pyplot as plt


def f(x, delta):
    return np.cos(x + delta) - np.cos(x)


def h(x, delta):
    n = 100
    h_arr = np.empty(delta.shape)
    for i in range(0, len(delta)):
        xi = np.linspace(x, x + delta[i], n)
        h_temp = -delta[i] * np.sin(x) - delta[i] ** 2 * np.cos(xi) / 2.
        diff = np.abs(h_temp - f(x, delta[i]))
        h_arr[i] = h_temp[diff == min(diff)][0]
    return h_arr


delta_arr = 10. ** np.array(range(-16, 1))

fig, ax = plt.subplots(layout="tight")
ax.scatter(delta_arr, np.abs(h(np.pi, delta_arr) - f(np.pi, delta_arr)), label="$x=\\pi$")
ax.scatter(delta_arr, np.abs(h(1e6, delta_arr) - f(1e6, delta_arr)), label="$x=10^6$")

ax.set(xscale='log', yscale='log', xlabel="$\\delta$", ylabel="$|\\cos(x+\\delta) - \\cos(x) - h(x,\\delta)|$")
ax.grid()
ax.legend()
plt.savefig("problem_5c.png", dpi=300)
# plt.show()
