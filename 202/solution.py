class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sq = [x**2 for x in range(10)]
        hascomputed = set()
        while n != 1:
            if n in hascomputed:
                return False
            hascomputed.add(n)
            nextn = 0
            while n > 0:
                nextn += sq[n % 10]
                n /= 10
            n = nextn
        return True
        
