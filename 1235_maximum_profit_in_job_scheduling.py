class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # top down
        # sort by start time
        lst = list(zip(startTime, endTime, profit))
        lst.sort(key=lambda x: x[0])

        dp = {}

        def rec(i):
            if i == len(lst):
                return 0
            if i in dp:
                return dp[i]
            # skip
            skip = rec(i + 1)

            # include
            include = 0
            # find the first interval that start after the current one end
            nxt = i + 1
            end = lst[i][1]
            while nxt < len(lst) and end > lst[nxt][0]:
                nxt += 1
            include = lst[i][2] + rec(nxt)

            dp[i] = max(skip, include)
            return dp[i]

        return rec(0)


"""
(1 3 50) (2 4 10) (3 5 40) (3 6 70)

(1 3 20) (2 5 20) (3 10 100) (4 6 70) (6 9 60)

dp = [ 80 100 130 60]
"""