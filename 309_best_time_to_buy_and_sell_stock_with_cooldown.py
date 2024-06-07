class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def rec(i, has_stock):
            if i >= len(prices):
                return 0
            if (i, has_stock) in dp:
                return dp[(i, has_stock)]
            res = 0
            if not has_stock:
                # buy
                buy = rec(i + 1, True) - prices[i]

                # skip buy
                skip = rec(i + 1, False)
                res = max(buy, skip)
            else:
                # sell
                sell = prices[i] + rec(i + 2, False)
                res = max(res, sell)

                # skip sell
                hold = rec(i + 1, True)
                res = max(res, hold)
            dp[(i, has_stock)] = res
            return res

        return rec(0, False)


"""
possible actions:
buy, skip buy, 
long then hold (skip sell)
sell
cool down

1       2       3       0       2
buy     hold    h       h       h
                                sell    => profit = 1
                        sell at loss
                sell    cool            => profit = 2
        sell    cool    buy     sell    => profit = 3


        sell

hold

skip


1       2       3       0       2

"""