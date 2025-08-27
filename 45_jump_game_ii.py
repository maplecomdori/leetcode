class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy
        left = right = 0  # current window
        count = 0

        while right < len(nums) - 1:
            furthest = left
            count += 1
            i = left
            for i in range(right + 1):
                furthest = max(furthest, i + nums[i])
                if furthest >= len(nums) - 1:
                    return count

            left = right + 1
            right = furthest

        return count

        # bottom up
        dp = [float("inf")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump >= len(nums) - 1:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], 1 + dp[i + jump])

        return dp[0]


"""
2   3   1   1   4
lr
    l   r
            l   r

2
lr

1   1
lr
    lr

---->----------->
2   3   1   1   4
                0
            1
        2
    3,2,1
2,3



---->----------->
------->
2   3   0   1   4   target
                0   4
            1       3
        0           3
    1               1
2                   0

"""