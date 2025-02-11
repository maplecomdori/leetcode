class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        hm = {}  # { nums[i]-i: count }

        num_good_pairs = 0
        for i, n in enumerate(nums):
            val = n - i
            if val not in hm:
                hm[val] = 1
            else:
                num_good_pairs += hm[val]
                hm[val] += 1

        return (len(nums) * (len(nums) - 1)) // 2 - num_good_pairs
