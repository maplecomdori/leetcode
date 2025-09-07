class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # bottom up
        total = sum(nums)
        if total % 2:
            return False

        half_total = total // 2
        dp = [[False] * (half_total + 1) for _ in range(len(nums) + 1)]
        # dp[row][sum] is true if the sum can be made with nums[0] ... nums[row]
        dp[0][0] = True
        for row in range(1, len(dp)):
            for col in range(half_total + 1):
                if col - nums[row - 1] < 0:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row - 1][col] \
                                   or dp[row - 1][col - nums[row - 1]]

        return dp[-1][-1]

        # top down
        total = sum(nums)
        if total % 2:
            return False

        half_total = total // 2
        dp = {}

        def rec(i, running_sum):
            if i == len(nums) or running_sum > half_total:
                return False
            if running_sum == half_total:
                return True
            if (i, running_sum) in dp:
                return dp[(i, running_sum)]

            # use nums[i]
            use = rec(i + 1, running_sum + nums[i])
            if use:
                return use
            # skip nums[i]
            skip = rec(i + 1, running_sum)

            dp[(i, running_sum)] = use or skip
            return dp[(i, running_sum)]

        return rec(0, 0)
