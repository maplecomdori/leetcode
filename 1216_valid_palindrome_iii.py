class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        dp = {}

        def rec(i, j, k):
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            if k < 0:
                return False
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1

            if i >= j:
                return True

            res = rec(i + 1, j, k - 1) or rec(i, j - 1, k - 1)
            dp[(i, j, k)] = res
            return res

        return rec(0, len(s) - 1, k)


"""
a   b   c   d   e   c   a
i                       j   # k=2
    i               j

        i           j       # move i k=1
            i   j
                            # move i or j => True           

    i           j           # move j
        i   j               # false k < 0


"""