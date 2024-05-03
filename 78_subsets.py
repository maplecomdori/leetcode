class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        builder = []

        def rec(i):
            if i == len(nums):
                res.append(builder[:])
                return
            # include
            builder.append(nums[i])
            rec(i + 1)
            builder.pop()

            # skip
            rec(i + 1)

        rec(0)

        return res


"""
[1,2,3]
1,2,3
1,2
1,3

"""