class Solution(object):
            
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1, 2]
        if n < len(arr):
            return arr[n-1]
        for i in range(2, n):
            arr.append(arr[i-1] + arr[i-2])
        return arr[-1]
