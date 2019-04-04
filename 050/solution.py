class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1.0/float(x)
        
        p = self.myPow(x, n/2)
        if n % 2 == 0:
            return p * p
        else:
            return p * p * x
