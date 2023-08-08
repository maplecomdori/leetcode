class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # left side is sorted
                if nums[left] <= target < nums[mid]:
                    # target is on the left side
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # right side is sorted
                if nums[mid] < target <= nums[right]:
                    # target is on the right side
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


