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


def bfs(grid):
    N = len(grid)
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ]
    costs = [[0]*(N) for _ in range(N)]
    isScan = [[False]*N for _ in range(N)]
    come_from = []
    for i in range(N):
        come_from.append([])
        for j in range(N):
            come_from[i].append((i, j))
    frontier = Queue()
    frontier.put((0, 0, costs[0][0]))
    isScan[0][0] = True
    while not frontier.empty():
        (x, y, costs[x][y]) = frontier.get()
        if x == N-1 and y == N-1:
            break
        for (dx, dy) in directions:
            x_new, y_new = x+dx, y+dy
            if (0 <= x_new < N) and (0 <= y_new < N) and grid[x_new][y_new] == 0 and costs[x_new][y_new] == 0 and isScan[x_new][y_new] == False:
                costs[x_new][y_new] = costs[x][y] + 1
                come_from[x_new][y_new] = (x, y)
                frontier.put((x_new, y_new, costs[x_new][y_new]))
                isScan[x_new][y_new] = True
    x, y = N-1, N-1
    path = [(x, y)]
    while True:
        if come_from[x][y] == (x, y):
            path.insert(0, come_from[x][y])
            break
        path.insert(0, come_from[x][y])
        x, y = come_from[x][y]
    return path


def main():
    g = grid(20)
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] = 0 if g[i][j] == 0 else 128

    path = bfs(g)
    for (x, y) in path:
        g[x][y] = 255

    plt.imshow(g, 'gray')
    plt.show()


if __name__ == '__main__':
    main()
