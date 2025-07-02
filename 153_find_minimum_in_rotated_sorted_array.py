class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        min_val = 10 ** 5

        while left <= right:
            mid = (left + right) // 2

            min_val = min(min_val, nums[mid])

            if nums[mid] < nums[right]:
                # right side is ordered => nums[mid] is minimum from mid to right
                # and search left further to find anything less than nums[mid]
                right = mid - 1
            else:
                left = mid + 1

        return min_val

"""
1   2   3   4   5
l       m       r   right side is ordered => minimum must be on the left side
lm  r
l

2   3   4   5   1
l       m       r   right side is not ordered => minimum must be to the right of nums[mid]
            lm  r
                lr  

3   4   5   1   2
l       m       r
            lm  r   mid > right => search right

4   5   1   2   3
l       m       r   mid < right => search left
lm  r               mid < right => search left

5   1   2   3   4
l       m       r   mid < right => search left

0
lr

1   2   3   4
l   m       r
lr

2   3   4   1
l   m       r
        lm  r
            lr
"""