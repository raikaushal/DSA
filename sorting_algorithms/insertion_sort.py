"""Insertion sort"""

"""take first element from un-sorted array  and insert at correct postion in sorted array
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i-1
        key = array[i]

        while (j >= 0) and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return array


array = [9, 8, 7, 1, 2, 3, 0]

# array = [7, 8, 9, 1, 4, 5]

print(insertion_sort(array))
