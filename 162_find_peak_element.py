class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left


"""
1   2
    X
l   r
    lr

2   1
X
l   r
lr

1   2   3   2
        X
l           r
        l   r

3   2   1
X
l       r
lr


1   3   2   1
    X

0   1   3   2   1
        X

1   0   1   2
            X

1   2   1   3   5   6   4
l           m           r

"""