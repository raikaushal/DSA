from array import array


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product*nums[j]
            res.append(product)
        return res


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
