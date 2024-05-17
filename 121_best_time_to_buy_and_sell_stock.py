class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        max_profit = 0

        for p in prices:
            profit = p - left
            max_profit = max(max_profit, profit)
            if p < left:
                left = p

        return max_profit


"""
7   1   5   3   6   4
lr
l   r
    lr
    l   r
    l       r
    l           r
    l               r
"""