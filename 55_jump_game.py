class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy: from the second last spot,
        # check if the target is reachable from the current index
        # update the target
        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            if i + n >= target:
                target = i

        return target == 0

        # bottom up

        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]

        # top down
        dp = {}
        dp[len(nums) - 1] = True

        def rec(i):
            if i == len(nums) - 1:
                return True
            if i in dp:
                return dp[i]
            for j in range(1, nums[i] + 1):
                if rec(i + j):
                    dp[i + j] = True
                    return True
            return False

        return rec(0)

