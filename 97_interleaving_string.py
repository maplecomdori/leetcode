class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # bottom up
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for p1 in range(len(s1), -1, -1):
            for p2 in range(len(s2), -1, -1):
                p3 = p1 + p2
                if p1 < len(s1) and s1[p1] == s3[p3] and dp[p1 + 1][p2]:
                    dp[p1][p2] = True
                if p2 < len(s2) and s2[p2] == s3[p3] and dp[p1][p2 + 1]:
                    dp[p1][p2] = True
        return dp[0][0]

        # top down
        # dp = {}
        # def rec(p1, p2, p3):
        #     if p3 == len(s3):
        #         if p1 < len(s1) or p2 < len(s2):
        #             return False
        #         else:
        #             return True
        #     if (p1,p2,p3) in dp:
        #         return dp[(p1,p2,p3)]
        #     use_s1 = False
        #     use_s2 = False
        #     if p1 < len(s1) and s1[p1] == s3[p3]:
        #         # compare with s1
        #         use_s1 = rec(p1 + 1, p2, p3 + 1)

        #     if p2 < len(s2) and s2[p2] == s3[p3]:
        #         # compare with s2
        #         use_s2 = rec(p1, p2 + 1, p3 + 1)

        #     dp[(p1,p2,p3)] = use_s1 or use_s2
        #     return dp[(p1,p2,p3)]

        # return rec(0,0,0)
