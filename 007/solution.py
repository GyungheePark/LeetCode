class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x >= 0:
            while x:
                result = result * 10 + x % 10
                x = x // 10
        else:
            x = -x
            while x:
                result = result * 10 + x % 10
                x = x //10
            result = -result
        
        if result >= -2**31 and result <= 2**31-1:
            return result
        else:
            return 0
