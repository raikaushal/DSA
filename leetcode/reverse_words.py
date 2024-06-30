from enum import Flag


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()
        res = ""
        for i in range(len(s)-1, -1, -1):
            if i == 0:
                res += s[i]
            else:
                res += s[i]+" "
        return res


s = "the      sky   is blue   "
print(Solution().reverseWords(s))
