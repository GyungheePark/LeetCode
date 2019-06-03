class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [2**31 for _ in range(amount + 1)]
        dp[0] = 0
        for c in coins:
            if c < len(dp):
                dp[c] = 1
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[amount] != 2**31:
            return dp[amount]
        else:
            return -1
