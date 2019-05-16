class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 1
        i = 0
        while i < len(s)-1 and s[i+1] == s[i]:
            i += 1
        j = i + 1
        if j == len(s):
            return result
        j += 1
        result += 1
        while j < len(s):
            cur = s[i:j]
            if s[j] in cur:
                i += cur.index(s[j])+1
                if i == j:
                    while i < len(s)-1 and s[i+1] == s[i]:
                        i += 1
                    j = i+1
                else:
                    j += 1
            else:
                j += 1
                if result < j-i:
                    result = j-i
        return result
