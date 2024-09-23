class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[right]:  # go right
                left = mid + 1
            else:  # go left
                right = mid - 1


"""
1   2   3   4   5
l       m       r   nums[l] <= nums[m] < nums[r] => return nums[l]

5   1   2   3   4   else go right
l       m       r

4   5   1   2   3
l       m       r   nums[m-1] > nums[m] => return nums[m]

3   4   5   1   2   left is sorted, right is not sorted => go right 
l       m       r   nums[mid] > nums[right] => go right
            l   r

2   3   4   5   1   nums[mid] > nums[right] => go right
l       m       r
            l   r

"""