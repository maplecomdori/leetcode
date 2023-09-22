class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use two pointers for s and t
        a = 0
        b = 0

        while b < len(t) and a < len(s):
            if s[a] == t[b]:
                a += 1
                b += 1
            else:
                b += 1

        return a == len(s)
