class Solution:
    def checkValidString(self, s: str) -> bool:
        # diff = number of '(' - number of ')'

        dp = {}

        def rec(i, diff):
            if diff < 0:
                return False
            if i == len(s):
                if diff == 0:
                    return True
                else:
                    return False
            res = False
            if (i, diff) in dp:
                return dp[i, diff]
            if s[i] == "(":
                res = rec(i + 1, diff + 1)
            elif s[i] == ")":
                res = rec(i + 1, diff - 1)
            elif s[i] == "*":
                res = rec(i + 1, diff) or rec(i + 1, diff + 1) or rec(i + 1, diff - 1)

            dp[(i, diff)] = res
            return res

        return rec(0, 0)