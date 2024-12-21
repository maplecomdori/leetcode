class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_idx = {0: -1}  # {remainder : idx}
        total = 0

        for i, n in enumerate(nums):
            total += n
            rem = total % k

            if rem in rem_idx:
                length = i - rem_idx[rem]
                if length > 1:
                    return True
            else:
                rem_idx[rem] = i
        return False

"""
a good subarray
    - length >= 2
    - sum of the subarray == k * X

23  2   4   6   7, k=6
    =====
23  25  29  35  42
5   1   5

1   2   -5  15  5, k=6, 6 12 18 24 30
1   3   -2  13  18
    ==========
1   3   -2  1

5   0   0   0 k=3 => True
    =====
2               {0:-1, 2:0}
2   2           {0:-1, 2:0} length = 2 => return True

"""