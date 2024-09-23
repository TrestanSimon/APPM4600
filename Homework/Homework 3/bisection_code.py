
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
