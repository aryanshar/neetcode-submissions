class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profit = 0
        for price in prices:
            min_buy = min(min_buy, price)
            profit_poss = price - min_buy
            profit = max(profit_poss, profit)
        return profit