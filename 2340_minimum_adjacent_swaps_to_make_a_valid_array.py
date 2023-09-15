class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        max_val = 0
        max_idx = -1
        min_val = 10 ** 5
        min_idx = 0

        # find leftmost min
        # find rightmost max
        for i, n in enumerate(nums):
            if n < min_val:
                min_val = n
                min_idx = i
            if n >= max_val:
                max_val = n
                max_idx = i

        count = 0
        count += min_idx
        count += (len(nums) - max_idx - 1)

        if min_idx > max_idx:
            count -= 1
        return count


"""
... min ... max ...

... max ... min ...


[1,1,1] => 0
"""

