"""Insertion sort"""

"""take first element from un-sorted array  and insert at correct postion in sorted array
"""


def insertion_sort(array):
    for i in range(len(array)):
        if i == 0:
            continue

        j = 0
        while (j < i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]

            j += 1
    return array


array = [9, 8, 7, 1, 2, 3, 0]

array = [7, 8, 9, 1, 4, 5]

print(insertion_sort(array))
