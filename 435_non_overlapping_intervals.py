class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        left = 0
        for right in range(1, len(intervals)):
            first_interval = intervals[left]
            second_interval = intervals[right]
            if first_interval[1] <= second_interval[0]:
                left = right
            else:
                # overlapping
                count += 1

        return count

"""
1   2   3   4
====
    ====
        ====
========


====
    ====
  =======
        ======
"""