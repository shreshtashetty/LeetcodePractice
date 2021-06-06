# 122. Best Time to Buy and Sell Stock II

'''
Kevin's solution: subtract next day's price from prev day's price if it is greater than the previous day's price.
The solution is correct not because you are selling on the days which are higher than the previous day but rather the loop adds up all potential gains.   So if for example the array is  [5, 7, 100] the best is to buy on day 1 where the price is 5 and sell on day three where the price is 100.  Kevin's solution adds the gains of day one to day two with the gains of day two to day three.  Even if selling and re buying on the same day is not allowed this is still correct.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
                
        return profit
                
        
