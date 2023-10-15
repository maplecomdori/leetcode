class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # BOTTOM UP APPROACH
        mod = 10 ** 9 + 7
        COLS = min(steps, arrLen)
        dp = [0] * COLS
        dp[-1] = 1

        for row in range(1, steps + 1):
            tmp = [0] * COLS
            for col in range(COLS):
                tmp[col] = dp[col]
                if col > 0:
                    tmp[col] += dp[col - 1]
                if col + 1 < COLS:
                    tmp[col] += dp[col + 1]
                tmp[col] %= mod
            dp = tmp
        return dp[-1]


"""
    arrLen
steps   1   0
        1   1
        2   2
        4   4

"""

    # TOP DOWN APPROACH
    # mod = 10 ** 9 + 7
    # left = 0
    # right = arrLen - 1
    # idx = 0

    # dp = {}

    # def rec(idx, rem):
    #     if idx < 0 or idx == arrLen:
    #         return 0
    #     if rem == 0:
    #         if idx == 0:
    #             return 1
    #         else:
    #             return 0
    #     key = f"{idx}-{rem}"
    #     if key in dp:
    #         return dp[key]
    #     right = rec(idx + 1, rem - 1)
    #     left = rec(idx - 1, rem - 1)
    #     stay = rec(idx, rem - 1)

    #     dp[key] = (right + left + stay) % mod
    #     return dp[key]

    # return rec(0, steps)

