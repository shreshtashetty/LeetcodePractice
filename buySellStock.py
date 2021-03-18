# 121. Best Time to Buy and Sell Stock
# refer to their 1 pass solution which is better than the brute force approach

import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = np.inf
        maxprofit = 0
        
        for i in range(len(prices)):
            
            if prices[i]<minprice:
                minprice = prices[i]
                
            elif prices[i]>minprice and prices[i]-minprice>maxprofit:
                maxprofit = prices[i]-minprice
        
        return maxprofit
        
