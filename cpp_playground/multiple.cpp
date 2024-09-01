#include <iostream>
using namespace std;

int sumMultiple36 (int n) {
    int x, sum = 0;
    while (x < n) {
        if (x % 3 == 0 || x % 5 == 0) {
            sum += x;
        }
    x += 1;
    }
    return sum;
}

int main() {
    int target = 0;
    cout << "Target:";
    cin >> target;
    cout << sumMultiple36(target) << endl;
    return 0;
}