class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        s1 = []
        s2 = []
        i = 0
        result = ''
        for s in S:
            if not s1:
                s1.append(s)
            else:
                if not s2:
                    if s == '(':
                        s2.append(s)
                        result += s
                    else:
                        s1.pop()
                else:
                    if s == '(':
                        s2.append(s)
                    else:
                        s2.pop()
                    result += s
        return result
