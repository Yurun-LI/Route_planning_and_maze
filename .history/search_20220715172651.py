import numpy as np
import pygame

maze = np.load("./maze.npy")


class Search:
    def __init__(self, maze):
        self.maze = maze
        if not len(maze):
            self.row = len(maze)
            if not len(maze[0]):
                self.col = len(maze[0])
