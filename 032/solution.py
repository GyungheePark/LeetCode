class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        longest = [0] * len(s)
        for i in range(len(s)):
            if i > 0:
                if s[i-1] == "(" and s[i] == ")":
                    longest[i] = longest[i-2] + 2
                elif s[i-1] == ")" and s[i] == ")" and (i - longest[i-1] - 1 >= 0 and s[i-longest[i-1]-1] == "("):
                    longest[i] = longest[i-1] + longest[i - longest[i-1]-2] + 2
        return max(longest)
                    
