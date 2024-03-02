class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = deque()

        while left < right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            if left_squared < right_squared:
                res.appendleft(right_squared)
                right -= 1
            else:
                res.appendleft(left_squared)
                left += 1

        res.appendleft(nums[left] ** 2)
        return res