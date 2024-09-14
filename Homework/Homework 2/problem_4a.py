import numpy as np


t = np.linspace(0, np.pi, 31, endpoint=True)
y = np.cos(t)

S = t @ y

print("the sum is: ", S)
