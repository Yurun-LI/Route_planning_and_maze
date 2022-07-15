import random
from re import S
import sys
from numpy import matrix
import pygame

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class Maze:
    def __init__(self, row: int, col: int, start: Point, end: Point):
        self.to_be_selected = []
        self.random_select_B = []
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
        self.maze = [[1 for j in range(col)] for i in range(row)]

        self.path_list = []

    def put_node_in_to_be_selected(self, node):
        for i in range(len(self.built_x)):
            nxt_node = Point(node.x+self.built_x[i], node.y+self.built_y[i])
            if 0 < nxt_node.x < self.row and 0 < nxt_node.y < self.col and nxt_node not in self.to_be_selected and self.maze[nxt_node.x][nxt_node.y] == 1:
                self.to_be_selected.append(nxt_node)
    
    def random_B(self,node:Point)->Point:
        self.random_select_B.clear()
        for i in range(len(self.built_x)):
            nxt_node = Point(node.x+self.built_x[i], node.y+self.built_y[i])
            if 0 < nxt_node.x < self.row and 0 < nxt_node.y < self.col and self.maze[nxt_node.x][nxt_node.y] == 0:
                self.random_select_B.append(nxt_node)
        return self.random_select_B[random.randint(0,len(self.random_select_B)-1)]
    def generate_maze(self):
        if len(self.to_be_selected) > 0:
            select_nodeA = self.to_be_selected[random.randint(0, len(self.to_be_selected)-1)]
            select_nodeB = self.random_B(select_nodeA)
            self.maze[select_nodeA.x][select_nodeA.y] = 0
            mid_x = int((select_nodeA.x+select_nodeB.x)/2)
            mid_y = int((select_nodeA.y+select_nodeB.y)/2)
            self.maze[mid_x][mid_y] = 0
            self.put_node_in_to_be_selected(select_nodeA)
            self.to_be_selected.remove(select_nodeA)
    
def main():
    row, col = 61,61
    start = Point(1,1)
    end = Point(row-2, col-2)
    maze = Maze(row,col,start,end)
    