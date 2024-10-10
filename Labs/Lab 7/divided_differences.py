import numpy as np


def dd_table(nodes, f_nodes):
    n = len(nodes)

    y = np.zeros((n, n))
    y[:, 0] = f_nodes
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = (y[j, i-1] - y[j+1, i-1]) / (nodes[j] - nodes[i+j])

    return y


def eval_dd_polynomial(x, nodes, dd):
    m, n = len(x), len(nodes)

    ptmp = np.zeros((n, m))
    ptmp[0] = 1.
    for i in range(n-1):
        ptmp[i+1] = ptmp[i] * (x - nodes[i])

    return np.sum([dd[0, i] * ptmp[i] for i in range(n)], axis=0)
