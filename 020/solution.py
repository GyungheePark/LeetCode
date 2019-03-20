class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if not stack:
                stack.append(p)
            elif p == '(' or p == '{' or p == '[':
                stack.append(p)
            else:
                if (p == ')' and stack[-1] == '(') or (p == '}' and stack[-1] == '{') or (p == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
