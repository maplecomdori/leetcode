class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        builder = []
        nums.sort()
        seen = set() # { tuple }

        def rec(i):
            if i == len(nums):
                tup = tuple(builder[:])
                if tup not in seen:
                    res.append(builder[:])
                    seen.add(tup)
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
0
[0]


1   2   2
[]  [1] [1,2] [1,2,2], [2], [2,2]

1
1   2
1   2   2   add
1   2   X   add
1   X   2   duplicate
1   X   X   add

X
X   2
X   2   2   add
X   2   X   Add
X   X   2   duplicate


"""