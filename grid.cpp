#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <time.h>
#include <unistd.h>


using namespace std;

void MainMenu();
void MenuGame(int num);
void Introduce();
void delay_sec(int sec) {
    time_t start_time, cur_time;
    time(&start_time);
    do {
        time(&cur_time);
    } while ((cur_time - start_time) < sec);
}
int main() {
    int i = 0, choice = 0, choice_2, choice_3;
    char isexit = ' ', choice_1 = ' ';
    bool Go_on = false, judge[4] = {false};

    cout << "\n\t大爷来玩呀~" << endl;
    for (int i = 0; i < 4; i++) {
        delay_sec(1);
        printf(".");
    }
    system("cls");
    Introduce();

    return 0;
}
