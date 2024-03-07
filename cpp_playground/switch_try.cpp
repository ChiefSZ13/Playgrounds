#include <iostream>
#include <string>
using namespace std;

int main() {
    int x;
    cout << "Enter a number:";
    cin >> x;
    switch (x){
        case 1:
            cout << "1 in switch";
            break;
        case 2:
            cout << "2 in switch";
            break;
        default:
            cout << "Default in switch";
    }
    return 0;
}