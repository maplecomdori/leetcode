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
        set_word = set(wordDict)
        dp = {}

        def rec(i):
            if i == len(s):
                return True

            if i in dp:
                # if dp[i]:
                #     return True
                if not dp[i]:
                    return False

            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr in set_word:
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


"""
[cat cats and sand dog]
c   a   t   s   a   n   d   d   o   g 
i   j
i       j
            i   j
            i           j
                            i       j
                                        i

i           j
                i       j
                            i       j
                                        i


"""
