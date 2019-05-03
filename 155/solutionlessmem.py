class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 2**31

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            if self.min <= x:
                self.stack.append(x)
            else:
                self.min = x
                self.stack.append(x)
        else:
            self.min = x
            self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        last = self.stack[-1]
        self.stack.pop()
        if last == self.min:
            newmin = 2**31
            for s in self.stack:
                if s < newmin:
                    newmin = s
            if newmin != last:
                self.min = newmin

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
