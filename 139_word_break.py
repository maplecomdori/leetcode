class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        set_word = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr in set_word:
                    # print(i, j)
                    dp[i] = dp[j]
                if dp[i]:
                    break

        return dp[0]

        # top down
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            word_set = set(wordDict)
            dp = {}

            def rec(i):
                if i == len(s):
                    return True
                if i in dp:
                    return dp[i]

                for j in range(i + 1, len(s) + 1):
                    substring = s[i:j]
                    if substring in word_set:
                        if rec(j):
                            dp[i] = True
                            return True
                dp[i] = False
                return False

            return rec(0)


"""
leetcode [leet code]



catsndog    [cats dog sand and cat san]

dogsand [and, sand, dog]


abcd [a abc b cd]
0   1   2   3   4
a   b   c   d
                T
            F
        T
    T
T

"""