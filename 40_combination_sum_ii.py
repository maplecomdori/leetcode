class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        builder = []

        def rec(start: int, rem: int):
            if rem == 0:
                result.append(builder.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                if rem >= candidates[i]:
                    builder.append(candidates[i])
                    rec(i + 1, rem - candidates[i])
                    builder.pop()
                else:
                    break

        rec(0, target)
        return result
