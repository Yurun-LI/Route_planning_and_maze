import random
import sys
import pygame


class Maze:
    def __init__(self, row, col, start, end):
        self.to_be_selected = []
        self.random_select = []
        self.path_list = []
        self.row = row
        self.col = col
        self.built_x = [0, 2, 0, -2]
        self.built_y = [2, 0, -2, 0]
        self.run_x = [0, 1, 0, -1]
        self.run_y = [1, 0, -1, 0]
        self.isVisited = [[False for j in range(col)] for i in range(row)]
        self.isVisited[start[0]][start[1]] = True
