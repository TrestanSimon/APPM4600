import numpy as np
import time


def driver():
    x = np.random.rand(4)
    y = np.random.rand(4)
    z = np.random.rand(4, 3)
    w = np.random.rand(3, 2)

    t0 = time.perf_counter()
    product_1 = dot_product(x, y)
    t1 = time.perf_counter()
    product_2 = x @ y
    t2 = time.perf_counter()
    print(f"the product is : {product_1} taking {t1 - t0} s")
    print(f"the product is : {product_2} taking {t2 - t1} s")

    t0 = time.perf_counter()
    product_1 = matrix_multiplication(z, w)
    t1 = time.perf_counter()
    product_2 = z @ w
    t2 = time.perf_counter()
    print(f"the product is : {product_1} taking {t1 - t0} s")
    print(f"the product is : {product_2} taking {t2 - t1} s")
    return


# Custom dot product code
def dot_product(x, y):
    return np.sum(x * y)


# Custom matrix multiplication code
def matrix_multiplication(x, y):
    n, m = x.shape[0], y.shape[1]
    product = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            product[i][j] = np.sum(x[i, :] * y[:, j])
    return product


driver()
