import numpy as np
import matplotlib.pyplot as plt


# Problem 1
def p9_cof(x):
    return x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512


def p9(x):
    return (x-2)**9


x_arr = np.arange(1.920, 2.080, 0.001)

fig, axs = plt.subplots(ncols=2, layout="tight", sharey=True)
axs[0].plot(x_arr, p9_cof(x_arr))
axs[1].plot(x_arr, p9(x_arr))

axs[0].set(title="$p(x)$ via coefficients", xlabel="$x$", ylabel="$p(x)$")
axs[0].grid()
axs[1].set(title="$p(x)$ via expression $(x-2)^9$", xlabel="$x$")
axs[1].grid()
plt.savefig("problem_1.png", dpi=300)
# plt.show()
