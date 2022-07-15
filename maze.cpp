#include "maze.h"
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <time.h>
using namespace std;

Maze::Maze(int l, int w) {
    int i, j;
    Map_Length = l, Map_Width = w;
    for (i = 0; i < Map_Length; i++) {
        for (j = 0; j << Map_Width; j++) {
            if (i == 0 || j == 0) {
                Map[i][j] = road;
            } else {
                Map[i][j] = wall;
            }
        }
    }

    for (i = 0; i < Map_Length; i++) {
        for (j = 0; j < Map_Width; j++) {
            Visited[i][j] = 0;
        }
    }

    front = rear = -1;
    top          = -1;
}
void Maze::CreateMap(int x, int y)   //创建地图
{
    int Direction[4][2] = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};   //定义四个方向
    int i, j, temp;
    for (i = 0; i < 4; i++)   //打乱四个方向
    {
        j               = rand() % 4;
        temp            = Direction[i][0];
        Direction[i][0] = Direction[j][0];
        Direction[j][0] = temp;
        temp            = Direction[i][1];
        Direction[i][1] = Direction[j][1];
        Direction[j][1] = temp;
    }

    Map[x][y] = road;   //选取[x][y]为路

    for (i = 0; i < 4; i++) {
        if (Map[x + 2 * Direction[i][0]][y + 2 * Direction[i][1]] == wall)   //任意两点之间有路
        {
            Map[x + Direction[i][0]][y + Direction[i][1]] = road;
            CreateMap(x + 2 * Direction[i][0], y + 2 * Direction[i][1]);
        }
    }
}
