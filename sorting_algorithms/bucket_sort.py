import math


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while (j >= 0) and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr


def bucket_sort(arr):
    buckets = round(math.sqrt(len(arr)))

    output = [[] for _ in range(buckets)]

    for element in arr:
        aprropriate_bucket = math.ceil(element*buckets/max(arr))
        print(element, aprropriate_bucket)
        output[aprropriate_bucket-1].append(element)

    for i in range(buckets):
        sorted_arr = insertion_sort(output[i])
        output[i] = sorted_arr

    result = []
    for i in range(buckets):
        for j in range(len(output[i])):
            result.append(output[i][j])

    return result


array = array = [5, 3, 4, 7, 2, 8, 6, 9, 1]
print(bucket_sort(array))
