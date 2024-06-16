def linear_search(arr, target):
    if len(arr) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8


print(linear_search(arr, target))
