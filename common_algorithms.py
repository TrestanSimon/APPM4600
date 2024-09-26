
def bisection(f, a, b, tol, n_max=1000):
    if f(a) * f(b) > 0:
        raise Exception("a and b are the same sign")

    for i in range(n_max):
        midpoint = (a + b) / 2.

        if f(a) * f(midpoint) > 0:
            a = midpoint
        else:
            b = midpoint
        if abs(a - b) <= tol:
            return midpoint, i+1

    raise Exception("Number of iterations exceeded n_max")


def fixedpt(f, p0, tol, n_max):
    for i in range(n_max):
        p1 = f(p0)
        if abs(p1 - p0) < tol:
            return p1
        else:
            p0 = p1

    raise Exception("Number of iterations exceeded n_max")


def newton(f, df, p0, tol, n_max):
    def g(x):
        return x - f(x) / df(x)
    return fixedpt(g, p0, tol, n_max)
