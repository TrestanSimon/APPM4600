import numpy as np
import matplotlib.pyplot as plt


def eval_lagrange(x, nodes, f_nodes):
    m, n = len(x), len(nodes)
    return np.sum(np.array([
        np.nanprod([
            (x - nodes[j]) / (nodes[k] - nodes[j])
            if k != j else np.ones(m)
            for j in range(n)
        ], axis=0) * f_nodes[k] for k in range(n)
    ]), axis=0)
