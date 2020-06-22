class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Since we can do multiple transactions, its a running stream
        of stock prices. Whenever the price is greater the next day,
        we sell and calculate profit. On every such instance (when we
        make profit), we keep on adding to 'profit'
        """
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
            else:
                pass
        return profit
