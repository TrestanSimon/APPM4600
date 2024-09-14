from matplotlib import pyplot as plt
import numpy as np


theta = np.linspace(0, 2.*np.pi, 1000, endpoint=True)

R = 1.2
dr = 0.1
f = 15.
p = 0.

x = R * (1. + dr * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1. + dr * np.sin(f * theta + p)) * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(aspect='equal', xlabel='$x(\\theta)$', ylabel='$y(\\theta)$')
plt.savefig("problem_4b_i.png", dpi=300)
# plt.show()
