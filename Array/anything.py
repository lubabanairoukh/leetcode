class Solution(object):
    
    def bestbuy(self, prices, i):
        for index in range(i, len(prices) - 1):
            if prices[index] < prices[index + 1]:
                return index
        return -1
    
    def bestsell(self, prices, i):
        for index in range(i, len(prices) - 1):
            if prices[index] > prices[index + 1]:
                return index
        return -1
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_sum = 0
        index = 0
        while index < len(prices) - 1:
            index_buy = self.bestbuy(prices, index)
            if index_buy == -1:
                return max_sum
            index_sell = self.bestsell(prices, index_buy + 1)
            if index_sell == -1:
                return max_sum
            max_sum += prices[index_sell] - prices[index_buy]
            index = index_sell + 1
        
        return max_sum
