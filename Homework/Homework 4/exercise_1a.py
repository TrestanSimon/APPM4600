import matplotlib.pyplot as plt
from exercise_1_constants import *


x_arr = np.linspace(0, x_bar, 100)
f_arr = f(x_arr)

fig, ax = plt.subplots()
ax.plot(x_arr, f_arr)
ax.set(
    title=f"Soil temperature vs depth",
    xlabel="depth [m]",
    ylabel="soil temperature [$\\degree$C]",
    xlim=[0, x_bar], ylim=[-17, 22]
)
ax.grid(lw=0.5, linestyle='--', c='k')
ax.axhline(0, lw=1, color='k')
plt.savefig("problem_1a.png", dpi=300)
# plt.show()
