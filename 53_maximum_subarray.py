class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float("-inf")
        cum_sum = 0

        for n in nums:
            cum_sum += n
            max_val = max(max_val, cum_sum)
            if cum_sum < 0:
                cum_sum = 0
        return max_val


"""
1

1   -2      => 1
1   -1

1   -2  3   => 3
1   -1  3

2   -2  3   => 3
2   0   3

3   -2  3   => 4
3   1   4


-1  -2      => -1
-2  -1      => -1
    reset
if cumulative sum < 0, better to start over
"""