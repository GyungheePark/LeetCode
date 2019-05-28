class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(2, len(dp)):
            j = 1
            while j **2 <= i:
                dp[i] = min(dp[i], dp[i - (j**2)] + 1)
                j += 1
        return dp[-1]
