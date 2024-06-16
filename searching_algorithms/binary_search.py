

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


def binary_search(arr, target):
    left = 0
    end = len(arr)-1
    mid = (left+end)//2
    while (arr[mid] != target):
        if arr[mid] < target:
            left = mid+1
        else:
            end = mid-1
        mid = (left+end)//2

    return mid


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9


print(binary_search(arr, target))
