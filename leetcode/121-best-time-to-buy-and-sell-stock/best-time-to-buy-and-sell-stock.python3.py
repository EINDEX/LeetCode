class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 99999999999999999
        maxprofit = 0
        
        for i in prices:
            if i < minprice:
                minprice = i
            elif (i - minprice) > maxprofit:
                maxprofit = i - minprice
        return maxprofit
        
        
