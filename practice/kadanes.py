
def longest_subaray_sum(arr):
    sum = 0
    maxi = arr[0]

    for i in range(1, len(arr)):
        sum += arr[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0

    print(maxi)


longest_subaray_sum([1, 2, 3, 4, 5])
