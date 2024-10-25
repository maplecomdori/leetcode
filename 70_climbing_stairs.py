class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up

        if n in (1, 2):
            return n
        dp = [0] * (n + 1)
        dp[-1] = 1
        dp[-2] = 1
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]

        # top down
        dp = {}

        def rec(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in dp:
                return dp[i]
            res = rec(i + 1) + rec(i + 2)
            dp[i] = res
            return res

        return rec(0)


"""
0   1   2   3
3   2   1   1

"""