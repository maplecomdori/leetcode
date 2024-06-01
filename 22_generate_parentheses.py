class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        builder = []

        def rec(n_open, n_close):
            if len(builder) == n * 2:
                res.append("".join(builder))
                return

            if n_open < n:
                builder.append("(")
                rec(n_open + 1, n_close)
                builder.pop()

            if n_close < n_open:
                builder.append(")")
                rec(n_open, n_close + 1)
                builder.pop()

        rec(0, 0)

        return res