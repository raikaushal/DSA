
def merge(arr, start, end, mid):
    length1 = mid-start+1
    length2 = end-mid
    arr_left = arr[start:mid+1]
    arr_right = arr[mid+1:end+1]

    i = 0
    j = 0
    k = start

    while i < length1 and j < length2:
        if arr_left[i] < arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while i < length1:
        arr[k] = arr_left[i]
        i += 1
        k += 1

    while j < length2:
        arr[k] = arr_right[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, end, mid)
        return arr


arr = [7, 6, 4, 5, 2, 3, 1, 0]

print(merge_sort(arr, 0, len(arr)-1))
