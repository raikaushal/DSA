def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


arr = [7, 9, 8, 4, 5, 1, 3, 0]

# print(bubble_sort(arr))
# print(selection_sort(arr))
print(insertion_sort(arr))
