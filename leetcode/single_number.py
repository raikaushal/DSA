

def single_number(nums):
    xor = 0
    for n in nums:
        xor ^= n
    return xor
