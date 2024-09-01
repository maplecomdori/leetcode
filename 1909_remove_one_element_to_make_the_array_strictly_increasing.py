class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed_once = False
        #compare with next element
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i+1]:
                if removed_once: return False
                removed_once = True
                # case #1 from test case #1 => just skip (remove curr ith)
                if i > 0 and nums[i-1] < nums[i+1] or i == 0:
                    continue

                # case #2 from test case #2 => carry the curr number forward
                # remove i+1
                else:
                    nums[i+1] = nums[i]

        return True
"""
1   2   10  5   7
        X
2   3   1   2
        X   X
2   1   3   
    X
2   1   3   4
    X
2   1
    X
2   1   1
    X   X
2   1   2
X

"""