#include <iostream>
using namespace std;

void* non_optimized_selection_sort(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[i]) {
                swap(arr[j], arr[i]);
            }
        }
    }
}

void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) {
    cout << array[i] << " ";
  }
  cout << endl;
}


int main() {
    int list_1[] = {3, 8, 1, 9, 8, 7, 3, 2, 4};
    int size1 = sizeof(list_1)/sizeof(list_1[0]);
    printArray(list_1, size1);
    non_optimized_selection_sort(list_1, size1);
    printArray(list_1, size1);
    return 0;
}