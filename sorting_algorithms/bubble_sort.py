"""bubble sort"""
from typing import List


"""compare two consective element from start if its greater swap
it will put highest element at last for 1 iteration
"""


def bubble_sort(array: List) -> List:
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


array = [9, 8, 7, 1, 2, 3]

array = [7, 8, 9, 1, 4, 5]

print(bubble_sort(array))
