class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def count_pairs(diff: int):
            # count number of pairs whose difference <= diff
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count

        # do binary search on the number, diff: difference of two numbers in a pair
        left = 0
        right = nums[-1] - nums[0]
        ans = right

        while left < right:
            # find 'diff' that can find exactly p pairs, where each pair has difference >= diff
            mid = (left + right) // 2
            count = count_pairs(mid)

            if count < p:
                # found less than p pairs using mid as diff, relax on 'diff' to find more pairs
                left = mid + 1
            else:
                # found more than p pairs using mid as diff, try reducing the number of pairs found by eliminating pairs found with the 'diff' that is too large
                right = mid

        return left
