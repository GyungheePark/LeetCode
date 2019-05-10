class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        digit = 1
        while s:
            result += digit * (ord(s[-1]) - 64)
            digit *= 26
            s = s[:-1]
        return result
