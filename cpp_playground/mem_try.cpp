#include <iostream>
#include <string>
using namespace std;

int main() {
    struct cars {
        string car1;
        string car2;
    };
    cars mycar;
    mycar.car1 = "Ferrari";
    mycar.car2 = "Red Bull";
    string &RB = mycar.car2;
    cout << mycar.car1 << " " << mycar.car2 << " " << RB << endl;
    cout << &mycar.car1 << " " << &mycar.car2 << " " << &RB << endl;
    if (mycar.car1 == "Ferrari") {
        int x1 = 1;
        cout << "Good Taste Man!\n";
    }
    switch (x1) {
        case 1:
            cout << "You chose SF";
            break;
        case 2:
            cout << "You chose Other";
            break;
    }
    return 0;
}