class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        result = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1:
                if dic[s[i]] >= dic[s[i+1]]:
                    result += dic[s[i]]
                    i += 1
                else:
                    result += (dic[s[i+1]] - dic[s[i]])
                    i += 2
            else:
                result += dic[s[i]]
                i += 1
        return result
