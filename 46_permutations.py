class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        builder = []
        res = []
        visited = set()

        def rec():
            if len(builder) == len(nums):
                res.append(builder[:])
                return

            for n in nums:
                if n not in visited:
                    builder.append(n)
                    visited.add(n)
                    rec()
                    visited.remove(n)
                    builder.pop()

        rec()
        return res


"""
1 2 3
1 3 2
2 1 3
"""