class Solution:
    def numDecodings(self, s: str) -> int:
        # 2 variables
        one = 1
        two = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                tmp = 0
            else:
                tmp = one

            if s[i] == "1" and i < len(s) - 1:
                tmp += two
            if s[i] == "2" and i < len(s) - 1 and s[i + 1] < "7":
                tmp += two
            two = one
            one = tmp
        return one

        # bottom up
        dp = [0] * ((len(s) + 1))
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if s[i] == "1" and i < len(s) - 1:
                dp[i] += dp[i + 2]
            if s[i] == "2" and i < len(s) - 1 and s[i + 1] < "7":
                dp[i] += dp[i + 2]

        return dp[0]

        # top down
        dp = [-1] * len(s)

        def rec(i):
            if i == len(s):
                return 1
            if dp[i] > 0:
                return dp[i]
            res = 0
            if s[i] != "0":
                res += rec(i + 1)
            if s[i] == "1" and i < len(s) - 1:
                res += rec(i + 2)

            if s[i] == "2" and i < len(s) - 1 and s[i + 1] < "7":
                res += rec(i + 2)
            dp[i] = res
            return res

        # return rec(0)


"""
2   2   6
0   0   0   1
        1
    1+1
2+1

0   6
0   0   1
    1
0

1   0   6
0   0   0   1
        1
    1
2

3   0   6 => 0
0   0   0   1
        1
    0

1   0   3   0   6

"""