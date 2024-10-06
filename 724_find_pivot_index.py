class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = [0]  # prefix_sum for augmented array: [0, nums, 0]

        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)
        prefix_sum.append(prefix_sum[-1])

        for idx in range(1, len(prefix_sum) - 1):
            if prefix_sum[idx - 1] == prefix_sum[-1] - prefix_sum[idx]:
                return idx - 1

        return -1


"""
    1   7   3   6   5   6
0   1   8   11  17  22  28  28

0   2   1   -1
0   2   3   2   2

    -1  1   2
0   -1  0   2   2
"""
