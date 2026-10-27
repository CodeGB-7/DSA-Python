class Solution(object):
    def maxProfit(self, prices):
        lowest=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<lowest:
                lowest=prices[i]
            profit=prices[i]-lowest
            if profit>maxprofit:
                maxprofit=profit
        return maxprofit        
