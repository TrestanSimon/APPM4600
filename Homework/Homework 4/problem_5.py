import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xscale

alpha = 1.1347241384015194


def fixedpt(f, p0, tol, n_max):
    p = [p0]
    print(abs(p0 - alpha))
    for i in range(n_max):
        p.append(f(p[i]))
        print(i+1, abs(p[-1] - alpha))
        if abs(p[-1] - p[-2]) < tol:
            return p

    raise Exception("Number of iterations exceeded n_max")


def newton(f, df, p0, tol, n_max):
    def g(x):
        return x - f(x) / df(x)
    return fixedpt(g, p0, tol, n_max)


def secant(f, p0, p1, tol, n_max):
    def g(x2, x1):
        return x1 - f(x1) * (x1 - x2) / (f(x1) - f(x2))
    p = [p0, p1]
    print(0, abs(p0 - alpha))
    print(1, abs(p1 - alpha))
    for i in range(n_max):
        p.append(g(p[i], p[i+1]))
        print(i+2, abs(p[-1] - alpha))
        if abs(p[-1] - p[-2]) < tol:
            return p


def f(x):
    return x**6 - x - 1


def fp(x):
    return 6*x**5 - 1


ne = np.array(newton(f, fp, 2, 1e-16, 1000))
se = np.array(secant(f, 2, 1, 1e-16, 1000))

fig, ax = plt.subplots()
ax.plot(np.abs(ne[:-1] - alpha), np.abs(ne[1:] - alpha), label="Newton's method")
ax.plot(np.abs(se[:-1] - alpha), np.abs(se[1:] - alpha), label="Secant method")
ax.set(
    xscale='log', yscale='log',
    xlabel="$|x_k-\\alpha|$", ylabel="$|x_{k+1}-\\alpha|$"
)
ax.legend()
ax.grid(lw=0.5, linestyle='--', c='k')
plt.savefig("problem_5b.png", dpi=300)
# plt.show()
