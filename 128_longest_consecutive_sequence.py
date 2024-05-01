class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_len = 0
        s = set(nums)
        used = set()

        # for i in range(len(nums)):
        for n in s:
            if n in used:
                continue

            while n - 1 in s:
                n = n - 1
            length = 1
            used.add(n)
            while n + 1 in s:
                length += 1
                n = n + 1
                used.add(n)
            max_len = max(max_len, length)

        return max_len


