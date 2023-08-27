class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        max_len = 0
        dp = [1] * len(pairs)

        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])

            max_len = max(max_len, dp[i])

        return max_len

