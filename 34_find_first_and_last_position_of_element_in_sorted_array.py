class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        # find the first occurence of 'target'
        first = -1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        # if not equal to target => return [-1, -1]
        if first == -1:
            return [-1, -1]

        # find the last occurence of 'target'
        left = 0
        right = len(nums) - 1

        last = -1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        # return first and last index of target
        return [first, last]

"""
5   7   7   8   8   10, target=8
l       m           r
            l   m   r
            lr

"""
