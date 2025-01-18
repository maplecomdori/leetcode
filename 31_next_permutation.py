class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find the first peak from the right
        peak = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                peak = i
                break

        if peak == len(nums):
            nums.reverse()
            return

        swap = peak - 1
        target = peak

        # find the number (least) greater than swap but less than peak
        for i in range(target + 1, len(nums)):
            if nums[swap] < nums[i] < nums[target]:
                target = i

        nums[swap], nums[target] = nums[target], nums[swap]
        nums[swap + 1:] = sorted(nums[swap + 1:])


"""
1   2   3
1   3   2

1   3   2
2   1   3

3   2   1 => not possible => reverse

1   1   5
1   5   1

2   7   4   3
7   2   4   3 => 7234

2   7   1   3
2   7   3   1

2   1   7   3
2   3   7   1

2   3   7   1
2   7   3   1 => 2713

"""