// 2 зад. Да се състави програма на C++, чрез която се извеждат елементите от
// масива с най-малката и най-голямата стойност.
// Вход:
// {79,72,13,14,15},{21,22,53,24,75},{31,57,33,34,35},{41,42,43,44,45},{59,52,53,54,55},{61,69,63,64,65}
// Изход: 13 79


#include <iostream>
using namespace std;

int main() {
    int rows, cols;

    cout << "Enter number of rows: ";
    cin >> rows;
    cout << "Enter number of columns: ";
    cin >> cols;

    int arr[rows][cols];

    cout << "Enter elements in format {a,b,c},{d,e,f},..." << endl;
    char ch;
    for (int i = 0; i < rows; i++) {
        cin >> ch;
        for (int j = 0; j < cols; j++) {
            cin >> arr[i][j];
            cin >> ch;
        }
        if (i < rows - 1) {
            cin >> ch;
        }
    }

    int min = arr[0][0];
    int max = arr[0][0];

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (arr[i][j] < min) {
                min = arr[i][j];
            }
            if (arr[i][j] > max) {
                max = arr[i][j];
            }
        }
    }

    cout << min << " " << max << endl;

    return 0;
}