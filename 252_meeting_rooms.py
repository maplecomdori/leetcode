class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()

        for i in range(len(intervals) - 1):
            first = intervals[i]
            second = intervals[i + 1]

            if second[0] < first[1]:
                return False
        return True


"""
=====
  =====
False

    ==========================
=====
        =========
                        ===========


"""