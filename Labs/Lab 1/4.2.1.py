import numpy as np


def driver():
    x = np.array([1, 0])
    y = np.array([999, 1])
    dp = dot_product(x, y)
    print("the dot product is : ", dp)
    print("the dot product is : ", x @ y)


def dot_product(x, y):
    return np.sum(x * y)


driver()
