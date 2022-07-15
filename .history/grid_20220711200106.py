import numpy as np
import matplotlib.pyplot as plt
from queue import Queue


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
    while True:
        g[i][j] = 0
        choice = 1 if np.random.random(1)[0] > 0.5 else 0
        if i == N-1 and j != N-1:
            j += 1
            g[i][j] = 0
        elif i != N-1 and j == N-1:
            i += 1
            g[i][j] = 0
        elif i == N-1 and j == N-1:
            g[i][j] = 0
            break
        else:
            if choice == 1:
                i += 1
            else:
                j += 1
            g[i][j] = 0
    return g


class LinkList():
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val


def search(grid, N):
    directions = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1],
    ]
    costs = [[0]*(N) for _ in range(N)]
    come_from = [[None] * (N) for _ in range(N)]
    frontier = Queue()
    frontier.put((0, 0, costs[0][0]))
    while not frontier.empty():
        curr = frontier.get()
        x, y = curr[0], curr[1]
        costs[x][y] = curr[2]

        if curr is (N-1, N-1, grid[N-1][N-1]):
            break
        for (dx, dy) in directions:
            x_new, y_new = curr[0]+dx, curr[1]+dy
            if (0 <= x_new < N-1) and (0 <= y_new < N-1) and grid[x_new][y_new] == 0 and costs[x_new][y_new] == 0:
                costs[x_new][y_new] = costs[x][y] + 1
                come_from[x_new][y_new] = (x, y)
                frontier.put(costs)
    x, y = N-1, N-1
    while True:
        if x == 0 and y == 0:
            grid[x][y] = 's'
            break
        grid[x][y] = 'x'
        (x, y) = come_from[x][y]
    return grid


def main():
    g = grid(5)
    for i in range(len(g)):
        for j in range(len(g[i])):
            print(grid[i][j], end='\t')
        print('\n')


if __name__ == '__main__':
    main()
