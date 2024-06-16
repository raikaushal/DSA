

def pivot(arr, pivot, end):
    swap_index = pivot
    for i in range(pivot+1, end+1):
        if arr[i] < arr[pivot]:
            swap_index += 1
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
    arr[swap_index], arr[pivot] = arr[pivot], arr[swap_index]
    return swap_index


def quick_sort(arr, start, end):
    if start < end:
        pivot_index = pivot(arr, start, end)
        quick_sort(arr, start, pivot_index-1)
        quick_sort(arr, pivot_index+1, end)
        return arr


arr = [1, 8, 9, 0, 7, 6, 5, 4, 3, 2]

print(quick_sort(arr, 0, len(arr)-1))
