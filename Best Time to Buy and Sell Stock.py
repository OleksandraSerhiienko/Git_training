def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: #checks if list of prices is ampty or not, if it is so then returns False
            return False
        min_price = prices[0] 
        max_profit = 0
        for i in prices:
            #print(i)
            min_price= min(min_price, i)
            max_profit = max(max_profit, i - min_price)
        return max_profit