class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i = len(prices) - 1
        maxprice = 0
        profit = 0
        while i >= 0:
            maxprice = max(maxprice, prices[i])
            profit = max(profit, maxprice - prices[i])
            i -= 1
        return profit
