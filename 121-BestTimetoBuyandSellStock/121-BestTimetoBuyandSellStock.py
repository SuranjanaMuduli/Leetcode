class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            min_price = min(min_price,p)
            profit = p - min_price
            max_profit = max(max_profit,profit)
        return max_profit
        # max_profit = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit,profit)
        # return max_profit

        

