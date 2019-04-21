class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        locmin, locmax = prices[0], 0
        result = 0
        for i in range(len(prices)):
            if locmax == 0:
                if prices[i] < locmin:
                    locmin = prices[i]
                elif prices[i] > locmin:
                    locmax = prices[i]
            else:
                if prices[i] < locmax:
                    result += (locmax-locmin)
                    locmin, locmax = prices[i], 0
                elif prices[i] > locmax:
                    locmax = prices[i]
        result += max(0, locmax - locmin)
        return result
