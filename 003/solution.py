class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            j = i
            while len(set(s[i:j+1])) == j+1-i and j < len(s):
                j += 1
            if result < j-i:
                result = j-i
            if len(s) - (i+1) <= result:
                break
        return result
