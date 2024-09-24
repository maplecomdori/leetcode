class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = len(nums1) - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1

        # copy over the remaining elements in nums2
        # no need to copy over the remaining elements in nums1, which must be already sorted
        while k >= 0 and j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


"""
1   2   3   0   0   0       2   5   6
        i           k               j
                    6
        i       k               j
        i   k   5           j
    i   k   3               j
i   k   2                   j
ik  2
1


1   2   8   0   0   0       3   4   6
                    8
                6
            4
        3


3   4   0   0               1   2
            4
        3
"""