#include <iostream>
using namespace std;

void print_array(int *array, int size) {
    for(int ii = 0; ii < size; ii++) {
        cout << array[ii] << " ";
    }
    cout << endl;
}

void swap(int *x, int *y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

void partition(int *array, int left, int right) {
    int pivot_idx = left;
    int pivot = array[left];
    while(left < right) {
        if(array[left] > pivot) {
            swap(&array[left], &array[right]);
            right--;
        } else {
            left++;
        }
    }
    if(array[left] > pivot) {
        swap(&array[pivot_idx], &array[left-1]);
    } else {
        swap(&array[pivot_idx], &array[left]);
    }
}

void qsort(int *array, int size) {
    partition(array, 0, size-1);
    print_array(array, size);
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

    qsort(array, size);
    delete [] array;
    return 0;
}
