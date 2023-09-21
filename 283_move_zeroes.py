class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start from rightmost zeros, switch towards right
        right = len(nums) - 1

        while right >= 0:
            if nums[right] == 0:
                idx = right
                while idx + 1 < len(nums) and nums[idx + 1] != 0:
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                    idx += 1
            right -= 1

