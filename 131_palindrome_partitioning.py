class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j

        res = []
        builder = []

        def rec(i):
            if i == len(s):
                res.append(builder[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    builder.append(s[i:j + 1])
                    rec(j + 1)
                    builder.pop()

        rec(0)
        return res


"""
a   a   b
a   a   b
aa  b

"""