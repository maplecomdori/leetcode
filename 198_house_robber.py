class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up
        dp = [0] * (len(nums) + 2)
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]
        # top down
        dp = [0] * len(nums)

        def rec(i):
            if i >= len(nums):
                return 0
            if dp[i]:
                return dp[i]
            rob = nums[i] + rec(i + 2)
            skip = rec(i + 1)

            dp[i] = max(rob, skip)
            return dp[i]

        return rec(0)


"""
1   2   3   1
1   X   3   X
        X   1

X   2   X   1
            X
    X   3   X

1   2   3   1   0   0
            max(1 + 0, 0) = 1
        max(3+0, 1) = 3
    max(2 + 1, 3) = 3
max(1 + 3, 3) = 4

"""