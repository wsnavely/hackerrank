#include <iostream>

using namespace std;

void print_array(int *array, int size) {
    for(int ii = 0; ii < size; ii++) {
        cout << array[ii] << " ";
    }
    cout << endl;
}

void insert(int *array, int idx, int (*compare)(int,int)) {
    int val = array[idx];
    while(idx > 0 && compare(val, array[idx-1]) < 0) {
        array[idx] = array[idx-1];
        idx--;
    }
    array[idx] = val;
}

int compare(int x, int y) {
    return x-y;
}

void isort(int *array, int size) {
    for(int ii = 1; ii < size; ii++) {
        insert(array, ii, compare);
        print_array(array, size);
    }
}

int main(int argc, char **argv) {
    int size;
    int *array;
    int ii;
    
    cin >> size;
    array = new int[size];
    for(ii = 0; ii < size; ii++) {
        cin >> array[ii];
    }

    isort(array, size);
    delete [] array;
    return 0;
}
