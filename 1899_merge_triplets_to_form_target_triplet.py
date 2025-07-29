class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        builder = [0, 0, 0]
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            builder[0] = max(builder[0], a)
            builder[1] = max(builder[1], b)
            builder[2] = max(builder[2], c)

            if builder == target:
                return True
        return False