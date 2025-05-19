class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        # calculate prefix sum of plates
        prefix_sum = []
        curr = 0
        for i in range(len(s)):
            curr += s[i] == "*"
            prefix_sum.append(curr)

        # store leftmost candle for each index
        leftmost_candle = []
        idx = -1
        for i in range(len(s)):
            if s[i] == "|":
                idx = i
            leftmost_candle.append(idx)

        # store rightmost candle for each index
        rightmost_candle = []
        idx = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "|":
                idx = i
            rightmost_candle.append(idx)
        rightmost_candle.reverse()

        for start, end in queries:
            # find the leftmost candle
            leftmost = rightmost_candle[start]
            # find rightmost candle
            rightmost = leftmost_candle[end]
            # count the number of plates between the two candles
            count = 0
            if 0 <= leftmost < len(s) and 0 <= rightmost < len(s):
                count = max(0, prefix_sum[rightmost] - prefix_sum[leftmost])
            res.append(count)

        return res

