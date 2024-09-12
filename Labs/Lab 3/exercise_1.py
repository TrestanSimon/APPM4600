from modified_bisection_example import bisection


tol = 1e-5

f = lambda x: x ** 2 * (x - 1)

points = {
    "a": (0.5, 2),
    "b": (-1, 0.5),
    "c": (-1, 2),
}

for letter, p in points.items():
    [astar, ier] = bisection(f, p[0], p[1], tol)
    print("\nFor problem", letter)
    print('the approximate root is', astar)
    print('the error message reads:', ier)
    print('f(astar) =', f(astar))


"""
a) The root x=1 was found
b) No root was found, since both f(-1) and f(0.5) are less than zero
c) The root x=1 was found

The algorithm is not able to find the root x=0 because the function does not fully cross the x-axis.
That is, f(x) is negative on both sides of f(0), so the bisection algorithm, which requires one positive and one negative f(x), fails.
"""
