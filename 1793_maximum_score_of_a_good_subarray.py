class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # start at index k, expand left or right, whichever is greater
        left = k
        right = k
        max_val = nums[k]
        min_val = nums[k]

        while left >= 0 or right < len(nums):
            score = min_val * (right - left + 1)
            max_val = max(max_val, score)

            if right + 1 < len(nums) and left - 1 >= 0:
                # can move both left and right
                if nums[right + 1] > nums[left - 1]:
                    right += 1
                    min_val = min(min_val, nums[right])
                else:
                    left -= 1
                    min_val = min(min_val, nums[left])
            elif right + 1 < len(nums):
                # can't move left anymore
                right += 1
                min_val = min(min_val, nums[right])
            elif left - 1 >= 0:
                # can't move right anymore
                left -= 1
                min_val = min(min_val, nums[left])
            else:
                # can't move to both left and right
                return max_val

