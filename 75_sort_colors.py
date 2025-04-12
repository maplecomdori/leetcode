class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # nums[:left] => all 0
        curr = 0
        right = len(nums) - 1 # nums[right+1:] => all 2

        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

"""
red(0) white(1) blue(2)

2   0   2   1   1   0
lc                  r
0   0   2   1   1   2
    lc          r
        lc      r
0   0   1   1   2   2
        lc  r
        l   cr
        l   r   c

"""