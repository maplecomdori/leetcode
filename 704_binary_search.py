class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

"""
0  1 2 3 4 5
-1 0 3 5 9 12, target = 9
l    m      r
       l m  r. target = 12
            lr

0  1 2 3 4 5
-1 0 3 5 9 12, target = 2
l    m.     r
lm r
   lr
r    l

"""