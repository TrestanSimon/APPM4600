from common_algorithms import bisection, newton
from exercise_1_constants import *


bi = bisection(f, 0, x_bar, tol, 1000)
print(bi[-1], len(bi))

ne = newton(f, fp, 0.01, tol, 1000)
print(ne[-1], len(ne)-1)

try:
    ne2 = newton(f, fp, x_bar, tol, 1000)
    print(ne2[-1], len(ne2)-1)
except Exception as e:
    print(e)
