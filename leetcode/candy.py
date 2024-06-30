class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)
        return [True if x < max_num else False for x in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(Solution().kidsWithCandies(candies, extraCandies))
