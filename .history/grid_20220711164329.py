import numpy as np
import matplotlib.pyplot as plt


def grid(N):
    np.random.seed(1)
    g = np.random.random((N, N))
    for i in range(N):
        for j in range(N):
            if g[i][j] > 0.5:
                g[i][j] = 1
            else:
                g[i][j] = 0
    return g


def main():
    g = grid(10)


if __name__ == '__main__':
    main()
