class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        builder = []
        nums.sort()
        def rec(i):
            res.append(builder[:])
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                builder.append(nums[j])
                rec(j + 1)
                builder.pop()

        rec(0)

        return res

"""
1   2   2
[]
1
1   2
1   2   2
1       2   duplicate

    2
    2   2
        2   duplicate => skip a number if it is the same as the prev


1   1   2   2
[]
1
1   1
1   1   2
1   1   2   2

1       2
1       2   2
1           2   duplicate skip the second 2

    1           duplicate skip the second 1
    1   2       duplicate skip the second 1
    1   2   2   duplicate skip the second 1



"""