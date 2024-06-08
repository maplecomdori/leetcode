class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(include_leftmost, include_rightmost)
        if len(nums) == 1:
            return nums[0]
        prevprev, prev = 0, 0
        for i in range(len(nums) - 1):
            temp = max(nums[i] + prevprev, prev)
            prevprev = prev
            prev = temp
        include_leftmost = prev

        nxt, nxtnxt = 0, 0
        for i in range(len(nums) - 1, 0, -1):
            temp = max(nums[i] + nxtnxt, nxt)
            nxtnxt = nxt
            nxt = temp
        include_rightmost = nxt
        return max(include_leftmost, include_rightmost)


"""
2   3   2
2   X   X
X   3   X



1   2   3   1
1   X   4   X
        X   X
X   2


"""