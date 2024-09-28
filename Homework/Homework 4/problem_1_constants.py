import numpy as np
from scipy.special import erf


tol = 1e-13

Ts = -15. # deg C
Ti = 20.  # deg C
alpha = 0.138e-6  # m^2/s
t = 5.184e6  # s

x_bar = 5  # m


def f(x):
    return Ts + (Ti - Ts) * erf(x / (2. * np.sqrt(alpha * t)))

def fp(x):
    return (Ti - Ts) * np.exp(-(x / (2. * np.sqrt(alpha * t)))**2) / np.sqrt(np.pi * alpha * t)
