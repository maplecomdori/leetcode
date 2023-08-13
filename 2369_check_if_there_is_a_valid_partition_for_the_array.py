class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        # bottom up
        dp = [False] * (len(nums) + 1)
        dp[-1] = True

        # check if the last two elements in the 'nums' is the same
        dp[-3] = True if nums[-1] == nums[-2] else False

        # start from the third last element
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] == nums[i + 1]:
                # two equal elements
                dp[i] = dp[i] or dp[i + 2]

            if nums[i] == nums[i + 1] == nums[i + 2]:
                # three equal elements
                dp[i] = dp[i] or dp[i + 3]

            if nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                # three consecutive elements
                dp[i] = dp[i] or dp[i + 3]

        return dp[0]

        # top down
        # dp = [False] * len(nums)
        # def rec(i):
        #     if i == len(nums):
        #         return True

        #     if dp[i]:
        #         return dp[i]

        #     two = False
        #     three = False
        #     consecutive = False
        #     if i < len(nums) - 1 and nums[i] == nums[i+1]:
        #         two = rec(i + 2)
        #     if i < len(nums) - 2 and nums[i] == nums[i+1] == nums[i+2]:
        #         three = rec(i + 3)
        #     if i < len(nums) - 2 and nums[i] + 1== nums[i+1] and nums[i+1] + 1 == nums[i+2]:
        #         consecutive = rec(i + 3)
        #     dp[i] = two or three or consecutive
        #     return dp[i]

        # return rec(0)