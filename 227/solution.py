class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def getNum(s, i):
            j = i+1
            while j < len(s) and s[j] not in '+-*/':
                j += 1
            return (int(s[i:j]), j)
        s.replace(' ', '')
        stack = []
        i = 0
        n, i = getNum(s, i)
        stack.append(n)
        while i < len(s):
            if s[i] == '*':
                i += 1
                n, i = getNum(s, i)
                stack.append(stack.pop() * n)
            elif s[i] == '/':
                i += 1
                n, i = getNum(s, i)
                stack.append(int(float(stack.pop()) / n))
            elif s[i] == '+':
                i += 1
                n, i = getNum(s, i)
                stack.append(n)
            else:
                i += 1
                n, i = getNum(s, i)
                stack.append(-n)
        result = 0
        for n in stack:
            result += n
        return result
