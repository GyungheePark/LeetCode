class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            prevmin = self.stack[-1][1]
            if prevmin <= x:
                self.stack.append([x, prevmin])
            else:
                for s in self.stack:
                    s[1] = x
                self.stack.append([x,x])
        else:
            self.stack.append([x,x])

    def pop(self):
        """
        :rtype: None
        """
        last = self.stack[-1]
        self.stack.pop()
        if last[0] == last[1]:
            newmin = 2**31
            for s in self.stack:
                if s[0] < newmin:
                    newmin = s[0]
            if newmin != last[0]:
                for s in self.stack:
                    s[1] = newmin

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
