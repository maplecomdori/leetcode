class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # two way solution
        all = set(nums)
        visited = set()
        max_val = 0

        for n in nums:
            if n in visited:
                continue

            visited.add(n)
            length = 1

            # count numbers that are greater
            curr = n
            while curr + 1 in all:
                length += 1
                visited.add(curr + 1)
                curr += 1
            # count number that are less
            curr = n
            while curr - 1 in all:
                length += 1
                visited.add(curr - 1)
                curr -= 1

            max_val = max(max_val, length)
        return max_val

        # one way solution
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


