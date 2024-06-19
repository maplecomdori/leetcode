class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        total = 0

        for i in range(len(nums)):
            while stack and stack[-1] > nums[i]:
                stack.pop()
            stack.append(nums[i])
            total += len(stack)

        return total

"""
1   4   2   5   3
1
    14, 4
        142,2
            1425,25,5
                14253,253,53,3
"""