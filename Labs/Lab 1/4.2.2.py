import numpy as np


def driver():
    x = np.array([
        [1, 0, 2],
        [0, 2, 0],
        [2, 0, 0]
    ])
    y = np.array([
        [1, 800],
        [9, 100],
        [0, 0]
    ])

    product = matrix_multiplication(x, y)
    print("the product is : ", product)
    return


def matrix_multiplication(x, y):
    n, m = x.shape[0], y.shape[1]
    product = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            product[i][j] = np.sum(x[i, :] * y[:, j])
    return product


driver()
