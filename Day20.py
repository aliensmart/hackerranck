#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
"""
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
"""
total_swaps = 0
for i in range(n):
    number_of_swaps = 0
    for j in range(n-1):
        if a[i]> a[j + 1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j +1] = tmp
            number_of_swaps += 1
    total_swaps +=number_of_swaps


    if(number_of_swaps == 0):
        break

print("Array is sorted in " +str(total_swaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
