class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == "+":
                r = stack.pop()
                l = stack.pop()
                stack.append(l + r)
            elif t == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)
            elif t == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(l * r)
            elif t == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(float(l) / r))
            else:
                stack.append(int(t))
        return stack[-1]
