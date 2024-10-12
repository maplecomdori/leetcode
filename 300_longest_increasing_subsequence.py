class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up
        dp = [1] * (len(nums))

        for i in range(len(nums) - 1, -1, -1):
            max_len = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(max_len, dp[j] + 1)
            dp[i] = max_len

        return max(dp)

        # top down
        # dp = {}
        # def rec(i, cur_max):
        #     if i == len(nums):
        #         return 0
        #     if (i, cur_max) in dp:
        #         return dp[(i, cur_max)]
        #     # skip
        #     res = rec(i + 1, cur_max)

        #     # include
        #     if nums[i] > cur_max:
        #         res = max(res, 1 + rec(i + 1, nums[i]))
        #     dp[(i, cur_max)] = res
        #     return res

        # ans = rec(0, float("-inf"))

        # return ans

        res = [0] * len(nums)
        dp = {}

        def rec(i):
            if i == len(nums):
                return 0
            if i in dp:
                return dp[i]
            max_len = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(max_len, 1 + rec(j))
            dp[i] = max_len
            return max_len

        for k in range(len(nums)):
            res[k] = rec(k)
        return max(res)


"""
10  9   2   5   3   7   101 18
                            1
                        1
                    2
                3
            3
        4
    2/4
2/4
"""