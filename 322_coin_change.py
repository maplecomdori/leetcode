class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # bottom-up
        # if amount == 0:
        #     return 0
        # dp = [float("inf")] * (amount + 1)
        # dp[0] = 0
        # for i in range(1, amount + 1):
        #     for c in coins:
        #         if i - c >= 0:
        #             dp[i] = min(dp[i], 1 + dp[i-c])

        # return dp[-1] if dp[-1] != float("inf") else -1

        # top-down
        if amount == 0:
            return 0

        dp = {}

        def rec(total):
            if total > amount:
                return float("inf")
            if total == amount:
                return 0
            if total in dp:
                return dp[total]

            min_val = float("inf")
            for c in coins:
                min_val = min(min_val, rec(total + c) + 1)

            dp[total] = min_val
            return min_val

        res = rec(0)
        return res if res != float("inf") else -1


"""
1   2   5, 11


"""