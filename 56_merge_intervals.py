class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last_end = res[-1][1]
            curr = intervals[i]

            if last_end < curr[0]:
                # not overlapping with the last interval, add
                res.append(curr)
            else:
                # overlapping with the last interval, expand the last interval
                res[-1][1] = max(res[-1][1], curr[1])

        return res


"""
1,3 2,6 8,10 15,18
    5   0   5   0
---
 ----
      ---


  ------
---
  ---



 -----
---
 -------

 ---------------
----
 --------


  --------
----
   -------

"""