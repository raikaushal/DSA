
def merge(arr, l, r, mid):
    l1 = mid-l+1
    l2 = r-mid

    arr_left = arr[l:mid+1]
    arr_right = arr[mid+1:r+1]

    i = 0
    j = 0
    k = l
    while (i < l1 and j < l2):
        if arr_left[i] < arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while (i < l1):
        arr[k] = arr_left[i]
        i += 1
        k += 1

    while (j < l2):
        arr[k] = arr_right[j]
        j += 1
        k += 1

    return arr


def mergeSort(arr, l, r):
    if l < r:
        mid = (l+r)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, r, mid)
        return arr


arr = [1, 2, 5, 8, 7, 4, 0]

print(mergeSort(arr, 0, len(arr)-1))
