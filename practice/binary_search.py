data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search_recursive(arr, left, right, target):
    if len(arr) == 0:
        return

    mid = (left+right)//2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search_recursive(arr, mid+1, right, target)
    else:
        return binary_search_recursive(arr, left, mid-1, target)


print(binary_search_recursive(data, 0, len(data), 8))
