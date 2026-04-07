class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1 
        while r < len(prices):
            profit = prices[r] - prices[l]

            if prices[l] > prices[r]:
                l = r

            if profit >= max_profit:
                max_profit = profit
            r += 1

        return max_profit