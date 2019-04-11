class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        while (r+1)**2 <= x:
            r += 1
        return r
