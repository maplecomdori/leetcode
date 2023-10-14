"""
You are given a 0-indexed integer array nums and a positive integer k.

We call an index i k-big if the following conditions are satisfied:

    There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
    There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].

Return the number of k-big indices.



Example 1:

Input: nums = [2,3,6,5,2,3], k = 2
Output: 2
Explanation: There are only two 2-big indices in nums:
- i = 2 --> There are two valid idx1: 0 and 1. There are three valid idx2: 2, 3, and 4.
- i = 3 --> There are two valid idx1: 0 and 1. There are two valid idx2: 3 and 4.

Example 2:

Input: nums = [1,1,1], k = 3
Output: 0
Explanation: There are no 3-big indices in nums.
"""


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        max_heap = []  # size k
        left = [False] * len(nums)  # left[i] = True if there are at least k elems less than left[i] to its left
        right = [False] * len(nums)

        # mark left[i] True if nums[i] has at least k elems less than nums[i] to its left
        for i in range(len(nums)):
            n = nums[i]
            if len(max_heap) == k and n > -max_heap[0]:
                left[i] = True
            heapq.heappush(max_heap, -n)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # mark right[i] True if nums[i] has at least k elems less than nums[i] to its right
        max_heap = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if len(max_heap) == k and n > -max_heap[0]:
                right[i] = True
            heapq.heappush(max_heap, -n)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        count = 0
        for i in range(len(left)):
            if left[i] and right[i]:
                count += 1
        return count


"""
k=2
0   1   2   3   4   5
2   3   6   5   2   3

[]
i=0 [2]
i=1 [2,3]
i=2 [2,3,6]
i=3 [2,3]
i=4 [2,2]
i=5 [2,2]

j=5 [3]
j=4 [3 2]
j=3 [5 3 2]
j=2 [6 3 2]
j=1 [3 3 2]
j=0 [3 2 2]
[2 2]

"""