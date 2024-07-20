
def pivot_function(arr, pivot, end):
    swap_index = pivot
    for i in range(pivot+1, end+1):
        if arr[i] < arr[pivot]:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
    arr[swap_index], arr[pivot] = arr[pivot], arr[swap_index]

    return swap_index


def quick_sort(arr, start, end):
    if start < end:
        pivot_index = pivot_function(arr, start, end)
        quick_sort(arr, start, pivot_index-1)
        quick_sort(arr,  pivot_index+1, end)
        return arr


arr = [9, 8, 0, 7, 6, 3, 2, 1, 4, 5]

print(quick_sort(arr, 0, len(arr)-1))
