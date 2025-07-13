class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_count = 0
        count = 0
        lst_start = []
        lst_end = []
        for start, end in intervals:
            lst_start.append(start)
            lst_end.append(end)

        lst_start.sort()
        lst_end.sort()

        i = 0
        j = 0

        while i < len(lst_start):
            start = lst_start[i]
            end = lst_end[j]

            if start < end:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_count = max(max_count, count)

        return max_count


"""
0   5   10  15  20  25  30
==========================
    ======
            ======

0   5   10  15  20  25  30
      ====
 ===
"""