class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def check(c1, c2):
            # returns true if c1 == c2 or c1 + 1 == c2
            if c1 == c2:
                return True
            if c1 == 'z' and c2 == 'a':
                return True
            if ord(c2) - ord(c1) == 1:
                return True
            return False

        p1, p2 = 0, 0

        while p1 < len(str1) and p2 < len(str2):
            if check(str1[p1], str2[p2]):
                p1 += 1
                p2 += 1
            else:
                p1 += 1

        return p2 == len(str2)

