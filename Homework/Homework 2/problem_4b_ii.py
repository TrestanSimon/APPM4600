from matplotlib import pyplot as plt
import numpy as np
from random import uniform


theta = np.linspace(0, 2.*np.pi, 1000, endpoint=True)
dr = 0.05

fig, ax = plt.subplots()

for i in range(10):
    R = i
    f = 2. + i
    p = uniform(0, 2)

    x = R * (1. + dr * np.sin(f * theta + p)) * np.cos(theta)
    y = R * (1. + dr * np.sin(f * theta + p)) * np.sin(theta)

    ax.plot(x, y)

ax.set(aspect='equal', xlabel='$x(\\theta)$', ylabel='$y(\\theta)$')
plt.savefig("problem_4b_ii.png", dpi=300)
# plt.show()
