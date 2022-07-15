import random
import sys
import pygame

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class Maze:
    def __init__(self, row: int, col: int, start: Point, end: Point):
        self.to_be_selected = []
        self.random_select = []
        self.path_list = []
        self.row = row
        self.col = col
        self.start = start
        self.end = end
        self.built_x = [0, 2, 0, -2]
        self.built_y = [2, 0, -2, 0]
        self.run_x = [0, 1, 0, -1]
        self.run_y = [1, 0, -1, 0]
        self.isVisited = [[False for j in range(col)] for i in range(row)]
        self.isVisited[start.x][start.y] = True
        self.matrix = [[1 for j in range(col)] for j in range(row)]

    def put_node_in_to_be_selected(self, node):
        for i in range