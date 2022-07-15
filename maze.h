#ifndef MAZE_H
#    define MAZE_H

const int MaxSize  = 100;
const int road     = 0;
const int wall     = 1;
const int Mouse    = 2;
const int End      = 3;
const int visited  = 4;
const int MaxSmall = 5;

class Maze {
private:
    int pos_x, pos_y;
    int Map_Length, Map_Width;
    int Visited[MaxSize][MaxSize];
    int rear, front;
    int top;

public:
    Maze(int l, int w);
    ~Maze();

public:
    int Map[MaxSize][MaxSize];
    void CreateMap(int, int);
    void Show_Map();
    void Display();
    void KeepMap();
    void Move();
    void Up();
    void Down();
    void Left();
    void Right();
    void EditMap();
    void Short();
    void SmallRoadDisplay(int x, int y);
};
#endif
#pragma once
