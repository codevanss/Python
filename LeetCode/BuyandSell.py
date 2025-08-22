class Solution:
    def maxprofit(self , prices: list[int]) -> list[int]:
        l ,r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = profit[r] - profit[l]
                maxP = max(maxP , profit)
            else:
                l = r
            r+=1
        return maxP