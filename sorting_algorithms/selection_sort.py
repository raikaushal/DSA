"""selection sort"""

"""find the minimum element in array 
swap with first element and move pointer to 1 position
"""


def selection_sort(array):
    pointer = 0
    while pointer < len(array):
        minimum = pointer
        for i in range(pointer, len(array)):
            if array[i] < array[minimum]:
                minimum = i

        array[pointer], array[minimum] = array[minimum], array[pointer]
        pointer += 1

    return array


array = [9, 8, 7, 1, 2, 3, 0]

array = [7, 8, 9, 1, 4, 5]

print(selection_sort(array))
