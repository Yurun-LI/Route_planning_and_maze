import numpy as np
import matplotlib.pyplot as plt


def grid(N):
    np.random.seed(1)
    grid = np.zeros((N, N))
    print(grid)


def main():
    grid(10)


if __name__ == '__main':
    main()
