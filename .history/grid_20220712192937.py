import random
from re import S
import sys
from numpy import matrix
import pygame
random.seed(2022)


class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def isSame(self, Point2):
        if self.x == Point2.x and self.y == Point2.y:
            return True
        else:
            return False

    def isInList(self, pointList: list):
        for point in pointList:
            if point.x == self.x and point.y == self.y:
                return True
        return False


def demo():
    ls = [Point(1, 2), Point(2, 3), Point(3, 4)]
    a = Point(1, 2)
    if a in ls:
        print("a zai ls limian")
    else:
        print("a is not in ls")


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
        self.maze = [[1 for j in range(col)] for i in range(row)]

        self.path_list = []

        # initialization
        self.maze[start.x][start.y] = 0
        self.put_point_in_to_be_selected(start)
        self.path_list.append(start)
        self.isVisited[start.x][start.y] = True

        pygame.init()
        self.screen = pygame.display.set_mode(
            (col*10, row*10), flags=pygame.RESIZABLE)
        pygame.display.set_caption("Maze Game")

    def draw_rect(self, x: int, y: int, color: str):
        pygame.draw.rect(self.screen, color, ((y*10, x*10, 10, 10)))

    def draw_maze(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.maze[i][j] == 1:
                    self.draw_rect(i, j, "grey")
                if self.maze[i][j] == 2:
                    self.draw_rect(i, j, "green")
                if self.maze[i][j] == 3:
                    self.draw_rect(i, j, "red")

    def put_point_in_to_be_selected(self, point: Point):
        for i in range(len(self.built_x)):
            nxt_point = Point(point.x+self.built_x[i], point.y+self.built_y[i])
            if 0 < nxt_point.x < self.row and 0 < nxt_point.y < self.col and self.maze[nxt_point.x][nxt_point.y] == 1:
                isInSelected = False
                for point in self.to_be_selected:
                    if nxt_point.isSame(point):
                        isInSelected = True
                if isInSelected == False:
                    self.to_be_selected.append(nxt_point)

    def random_B(self, point: Point) -> Point:
        self.random_select_B.clear()
        for i in range(len(self.built_x)):
            nxt_point = Point(point.x+self.built_x[i], point.y+self.built_y[i])
            if 0 < nxt_point.x < self.row and 0 < nxt_point.y < self.col and self.maze[nxt_point.x][nxt_point.y] == 0:
                self.random_select_B.append(nxt_point)
        return self.random_select_B[random.randint(0, len(self.random_select_B)-1)]

    def generate_maze(self):
        if len(self.to_be_selected) > 0:
            select_nodeA = self.to_be_selected[random.randint(
                0, len(self.to_be_selected)-1)]
            select_nodeB = self.random_B(select_nodeA)
            self.maze[select_nodeA.x][select_nodeA.y] = 0
            mid_x = int((select_nodeA.x+select_nodeB.x)/2)
            mid_y = int((select_nodeA.y+select_nodeB.y)/2)
            self.maze[mid_x][mid_y] = 0
            self.put_point_in_to_be_selected(select_nodeA)
            self.to_be_selected.remove(select_nodeA)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.key == pygame.KEYDOWN:
                #     if event.key == pygame.K_q:
                #         pygame.quit()
                #         sys.exit()
            self.screen.fill("white")
            self.generate_maze()
            self.draw_maze()
            pygame.display.flip()
            pygame.time.Clock().tick(1000)


def main():
    row, col = 61, 61
    start = Point(1, 1)
    end = Point(row-2, col-2)
    maze = Maze(row, col, start, end)
    maze.run()


if __name__ == '__main__':
    demo()
