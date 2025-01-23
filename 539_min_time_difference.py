class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # TODO bucket sort solution

        # convert to numeric minutes
        lst_minutes = []
        for time in timePoints:
            lst = time.split(":")
            lst_minutes.append(int(lst[0]) * 60 + int(lst[1]))
        lst_minutes.sort()

        min_diff = float("inf")
        for i in range(len(lst_minutes) - 1):
            min_diff = min(min_diff, lst_minutes[i + 1] - lst_minutes[i])

        # find the difference between the latest time and (earliest time + 60 * 24)
        min_diff = min(min_diff, abs(1440 + lst_minutes[0] - lst_minutes[-1]))
        return min_diff


"""
00:00   23:59
0       1339
"""