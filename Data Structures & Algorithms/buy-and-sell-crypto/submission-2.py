class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if prices[r] < prices[l]:
                l = r
            r +=1 

        
        max_profit = max(0, max_profit)

        return max_profit