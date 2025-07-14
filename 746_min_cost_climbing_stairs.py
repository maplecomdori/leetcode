class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)

        for i in range(len(dp) - 3, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
        return min(dp[0], dp[1])

        cache = {}

        def rec(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]

            res = min(rec(i + 1), rec(i + 2)) + cost[i]
            cache[i] = res

            return res

        return min(rec(0), rec(1))
