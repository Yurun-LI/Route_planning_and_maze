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
    i = 0
    j = 0
    grid[i][j] = 0
    while i != N-1 and j != N-1:
        grid[i][j] = 0
        if np.random.random(1)[0] > 0.5:
            i += 1
        else:
            j += 1
        grid[i][j] = 1
    return g


def main():
    g = grid(10)
    print(g)


if __name__ == '__main__':
    main()
