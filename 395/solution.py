from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        
        i = 0
        result = 0
        while i < len(s):
            j = i
            while j < len(s):
                if dic[s[j]] < k:
                    result = max(result, self.longestSubstring(s[i:j], k))
                    i = j + 1
                    while i < len(s) and dic[s[i]] < k:
                        i += 1
                    break
                else:
                    j += 1
            if j == len(s):
                if i == 0:
                    result = len(s)
                else:
                    result = max(result, self.longestSubstring(s[i:j], k))
                break
        return result
