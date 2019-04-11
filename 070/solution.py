class Solution(object):
    arr = []
    def init(self, n):
        self.arr = [0, 1, 2]
        for _ in range(n-2):
            self.arr.append(0)
            
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not self.arr:
            self.init(n)
        
        if self.arr[n] > 0:
            return self.arr[n]
        
        if self.arr[n-1] == 0:
            self.arr[n-1] = self.climbStairs(n-1)
        if self.arr[n-2] == 0:
            self.arr[n-2] = self.climbStairs(n-2)
        return self.arr[n-1] + self.arr[n-2]
