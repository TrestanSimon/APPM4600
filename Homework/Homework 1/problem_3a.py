import numpy as np
from scipy.optimize import minimize_scalar


x1 = 1


def fun(x):
    # Negative sign added to get function maximum
    return -1. * (1./6.) * ((3. - 9.*x**2) * np.cos(x) + (1. - 17.*x + x**3) * np.sin(x)) * x1**3


res = minimize_scalar(fun, bounds=(0., x1), method='bounded')
print(res.x, abs(res.fun))
