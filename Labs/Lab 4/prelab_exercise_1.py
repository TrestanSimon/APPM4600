import numpy as np


def order_of_convergence(p, phat):
    return (np.log(np.abs(phat[3] - p) / np.abs(phat[2] - p)) /
            np.log(np.abs(phat[2] - p) / np.abs(phat[1] - p)))
