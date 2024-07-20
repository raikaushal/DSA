def merge(arr, left, right, mid):
    l1 = mid-left+1
    l2 = right-mid

    arr_left = arr[left:mid+1]
    arr_right = arr[mid+1:right+1]

    i = 0
    j = 0
    k = left

    while i < l1 and j < l2:
        if arr_left[i] < arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while i < l1:
        arr[k] = arr_left[i]
        i += 1
        k += 1
    while j < l2:
        arr[k] = arr_right[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, right, mid)
        return arr


arr = [9, 8, 6, 7, 4, 5, 3, 2, 1, 0]
left = 0
right = len(arr)-1

print(merge_sort(arr, left, right))
