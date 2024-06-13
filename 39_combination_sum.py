class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        builder = []
        candidates.sort()

        def rec(j, total):
            if total == target:
                res.append(builder[:])
                return
            if total > target:
                return

            for i in range(j, len(candidates)):
                builder.append(candidates[i])
                rec(i, total + candidates[i])
                builder.pop()

        rec(0, 0)

        return res


"""
2   3   6   7, target = 7

2222 X
223 yes
226 X
227 X
232 => duplicate, shouldn't be allowed
233 X
236
237 X
26* X
27 X

322 => duplicate shouldn't be allowed
"""