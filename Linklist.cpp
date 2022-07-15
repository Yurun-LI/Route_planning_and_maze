#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
typedef struct ListNode {
    double value;
    struct ListNode* next;
    ListNode(int v, ListNode* nx = nullptr) {
        value = v;
        next  = nx;
    }
} node;


int main(int argc, char* argv[]) {
    node* head = new node(1);
    node* ptr  = head;
    int a[]    = {1, 2, 3, 4, 5};
    int length = 5;
    while (--length) {
        node* q   = new node(a[length - 1]);
        ptr->next = q;
        ptr       = ptr->next;
    }
    node* ptr2 = head;
    while (ptr2 != nullptr) {
        cout << ptr2->value;
        ptr2 = ptr2->next;
    }
}
