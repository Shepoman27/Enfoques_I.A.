import numpy as np
def AQ(X, Y, k):
    n, m = X.shape
    V = [set(range(k)) for j in range(m)]
    H = []
    while len(Y) > 0:
        vio = np.zeros(n, dtype=bool)
        for j in range(len(V)):
            h = V.copy()
            for v in V[j]:
                h[j] = {v}
                yh = np.array([all(xh == x) for xh, x in zip(H, X)])
                yh[h[j] != set(X[:, j])] = False
                if any(yh):
                    vio[yh] = True
                elif np.all(yh == False):
                    H.append(h)
                    yh = np.array([all(xh == x) for xh, x in zip(H, X)])
                    vio[yh] = True
        if np.all(vio):
            break
        Y = Y[~vio]
        X = X[~vio, :]
    return H

X = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
])
Y = np.array([0, 0, 0, 1, 1, 1, 1, 1])
H = AQ(X, Y, 2)
