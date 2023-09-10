class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # bottom up
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, len(dp)):

            for n in nums:
                # try all numbers that you can add without going over the target
                # dp[4] = dp[3-1] + dp[3-2] + dp[3-3] for the example 1 [1,2,3]
                if i - n >= 0:
                    dp[i] += dp[i - n]

        return dp[-1]

        # top down
        dp = {}

        def rec(total):
            if total == target:
                return 1
            if total > target:
                return 0
            if total in dp:
                return dp[total]
            count = 0

            for j in range(len(nums)):
                if total + nums[j] <= target:
                    count += rec(total + nums[j])
            dp[total] = count
            return count

        return rec(0)


"""     Target
0   1   2   3   4
1
    1
        2           = 1 + 1 = dp(2-1) + dp(2-2) + dp(2-3)
            4       = 1 + 1 + 2
                7   = 1 + 2 + 4
"""

"""
1   2   3

3   1   2
3 1
1 3
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2

"""