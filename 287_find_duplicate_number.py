class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find cycle
        fast = nums[0]
        slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow


'''
1   2   3   4   5   number

0   1   2   3   4   index
==========================
1   3   4   2   2   nums

slow    fast
1       1
3       2
2       2
4       4
====


'''