class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] == nums[right]:
                # can't determine to go right or left, make the search space narrower
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                # left side is sorted
                if nums[left] <= target < nums[mid]:
                    # target is within the left side
                    right = mid - 1
                else:
                    # target is not within the left side, check the right side
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # right side is sorted
                if nums[mid] < target <= nums[right]:
                    # target is within the right side
                    left = mid + 1
                else:
                    # target is not within the right side, check the left side
                    right = mid - 1

        return False
