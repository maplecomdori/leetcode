# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = n
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            is_bad_version = isBadVersion(mid)
            if is_bad_version is True:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


"""
            bad
1   2   3   4   5
l       m       r
            lm  r




... true    true    true    false
                     X
"""