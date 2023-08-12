class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # top down
        dp = {}

        def rec(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i == len(coins):
                return 0
            key = (i, total)
            if key in dp:
                return dp[key]

            # skip using the current coin
            skip = rec(i + 1, total)

            # use the current coin
            use = rec(i, total + coins[i])
            dp[key] = skip + use
            return skip + use

        return rec(0, 0)

        # bottom up

        # dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # for i in range(len(coins) + 1):
        #     dp[i][0] = 1

        # for i in range(1, len(coins) + 1):
        #     for j in range(1, amount + 1):
        #         coin = coins[i-1]
        #         amt = j
        #         if coin > amt:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-coin]

        # return dp[-1][-1]