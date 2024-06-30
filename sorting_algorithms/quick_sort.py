

import pprint


def pivot_function(arr, pivot_index, right_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, right_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index]

    arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
    return swap_index


def quick_sort(arr, l, r):
    if l < r:
        pivot_index = pivot_function(arr, l, r)
        quick_sort(arr, l, pivot_index-1)
        quick_sort(arr, pivot_index+1, r)
    return arr


arr = [9, 8, 7, 4, 2, 1, 0]

# print(quick_sort(arr, 0, len(arr)-1))


dict = {
    "A": ["B", "C", "D"],
    "B": ["B", "C", "D"],
    "C": ["B", "C", "D"],
    "D": ["B", "C", "D"]
}


pprint.pp(dict)
