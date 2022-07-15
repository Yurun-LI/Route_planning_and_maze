#include <cstdio>
#include <ctime>
#include <iostream>
#include <queue>
#include <vector>


using namespace std;
typedef struct Node {
    int x;
    int y;
    Node* father = NULL;
} node;

#define down 1
#define right 2
#define left 4
#define up 8
class Search {
public:
    Search(int row, int col);
    ~Search(){};
    void getMaze();
    void bfs(node start, node terminal);
    void dfs();
    void aStar();

private:
    int m_col, m_row;
    int x_num, y_num;
    vector< vector<int> > grid;
    vector<int> block_row;
    vector<int> block_col;
    vector<int> block_direct;
    void push(int x, int y, int direct);
    int count();
};
void Search::push(int x, int y, int direct) {
    Search::block_row.push_back(x);
    Search::block_col.push_back(y);
    Search::block_direct.push_back(direct);
}
int Search::count() {
    int cnt = 0;
    if (x_num + 1 <= m_row) {
        push(x_num + 1, y_num, down);
        cnt++;
    }
    if (y_num + 1 <= m_col) {
        push(x_num, y_num + 1, right);
        cnt++;
    }   // right
    if (x_num - 1 >= 1) {
        push(x_num - 1, y_num, up);
        cnt++;
    }   // up
    if (y_num - 1 >= 1) {
        push(x_num, y_num - 1, left);
        cnt++;
    }   // left
    return cnt;
}
void Search::getMaze() {
    for (int i = 0; i < m_row; i++) {
        for (int j = 0; j < m_col; j++) {
            if (grid[i][j] == 2) {
                cout << ". ";
            } else {
                cout << "# ";
            }
        }
        cout << endl;
    }
    cout << endl;
}
void Search::bfs(node start, node terminal) {

    queue<node> q;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    int route_length[m_row][m_col];
    for (int i = 0; i < m_row; i++) {
        for (int j = 0; j < m_col; j++) {
            route_length[i][j] = 999;
        }
    }
    node *now, *next;
    *now                           = start;
    now->father                    = now;
    route_length[start.x][start.y] = 0;
    q.push(*now);
    cout << "开始广度优先搜索路径" << endl;

    while (!q.empty()) {
        //当队列不为空, 则逐个pop出队列元素.
        *now = q.front();
        cout << "子节点:" << now->x << "," << now->y << "\t父节点:" << now->father->x << "," << now->father->y << endl;
        // cout << "当前出队节点为(" << now.x << "," << now.y << ")" << endl;
        q.pop();
        //终止条件
        if (now->x == terminal.x && now->y == terminal.y) {
            //如果队列中元素坐标为终点坐标,则打印路径
            cout << "到达终点坐标, 准备输出路径" << endl;

            for (int i = 0; i < m_row; i++) {
                for (int j = 0; j < m_col; j++) {
                    cout << route_length[i][j] << "\t";
                }
                cout << endl;
            }
            return;
        }
        //否则依次计算周围网格的最短路径
        for (int i = 0; i < 4; i++) {
            next    = new node;
            next->x = now->x + dx[i];
            next->y = now->y + dy[i];
            //要想继续走, 下一个位置首先得不越界, 可通行, 并且下一个位置没走过或者
            if ((next->x >= 0 && next->x < m_row && next->y >= 0 && next->y < m_row) && (grid[next->x][next->y] == 2) && (route_length[next->x][next->y] > route_length[now->x][now->y] + 1)) {
                route_length[next->x][next->y] = route_length[now->x][now->y] + 1;
                next->father                   = now;
                q.push(*next);
            }
        }
    }
}

Search::Search(int row, int col) {
    m_col = col;
    m_row = row;
    x_num = 1;
    y_num = 1;
    int a[m_row + 2][m_col + 2];
    node start, ex;
    start.x = 1;
    start.y = 1;
    ex.x    = row;
    ex.y    = col;
    for (int i = 0; i <= m_row + 1; i++) {
        for (int j = 0; j <= m_col + 1; j++) {
            a[i][j] = 1;   // wall
        }
    }
    srand((unsigned)time(NULL));
    count();
    a[1][1] = 2;
    while (block_row.size()) {
        int num     = block_row.size();
        int randnum = rand() % num;
        x_num       = block_row[randnum];
        y_num       = block_col[randnum];
        switch (block_direct[randnum]) {   //选择一个方向进行后续操作，起始点 邻块 目标块 三块区域在同一直线上 随后移动到目标块的位置
        case down: {
            x_num = block_row[randnum] + 1;
            y_num = block_col[randnum];
            break;
        }
        case right: {
            x_num = block_row[randnum];
            y_num = block_col[randnum] + 1;
            break;
        }
        case left: {
            x_num = block_row[randnum];
            y_num = block_col[randnum] - 1;
            break;
        }
        case up: {
            x_num = block_row[randnum] - 1;
            y_num = block_col[randnum];
            break;
        }
        }
        if (a[x_num][y_num] == 1) {
            a[block_row[randnum]][block_col[randnum]] = 2;
            a[x_num][y_num]                           = 2;
            count();
        }
        block_row.erase(block_row.begin() + randnum);
        block_col.erase(block_col.begin() + randnum);
        block_direct.erase(block_direct.begin() + randnum);
    }
    // for (int i = 0; i <= row + 1; i++) {
    //     for (int j = 0; j <= col + 1; j++) {
    //         if (a[i][j] == 2) {
    //             printf(". ");
    //         } else {
    //             printf("# ");
    //         }
    //     }
    //     printf("\n");
    // }
    cout << "\nMaze established" << endl;
    for (int i = 1; i <= row; i++) {
        grid.push_back(vector<int>());
    }
    for (int i = 1; i <= m_col; i++) {
        for (int j = 1; j <= m_row; j++) {
            grid[j - 1].push_back(a[j][i]);
        }
    }
    Search::getMaze();
}

int main(int argc, char* argv[]) {
    Search s(11, 11);
    node start, terminal;
    start.x    = 0;
    start.y    = 0;
    terminal.x = 11 - 1;
    terminal.y = 11 - 1;
    s.bfs(start, terminal);

    return 0;
}
