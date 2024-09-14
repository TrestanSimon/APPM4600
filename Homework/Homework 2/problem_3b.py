from math import e
import numpy as np


def expm1v1(x):
    y = e ** x
    return y - 1


def expm1v2(x):
    return x + x**2/2. + x**3/6.


x = 9.999999995000000e-10
print(expm1v1(x))
print((expm1v1(x) - np.expm1(x))/np.expm1(x))
print(expm1v2(x))
print(format(np.expm1(x), '.40g'))
print(format(abs((expm1v2(x) - np.expm1(x))/np.expm1(x)), '.20g'))

