class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        res = []
        if not intervals:
            # empty list
            res.append(newInterval)
        elif new_end < intervals[0][0]:
            # insert at the front
            res = [newInterval] + intervals
        elif intervals[-1][1] < new_start:
            # insert at the end
            res = intervals + [newInterval]
        else:
            # insert in the middle somewhere

            for i in range(0, len(intervals)):
                curr = intervals[i]

                # not overlapping with any
                if i > 0 and intervals[i - 1][1] < new_start and new_end < curr[0]:
                    res.append(newInterval)
                    res.extend(intervals[i:])
                    break

                # no overlapping with new and prev
                elif new_end < curr[0]:
                    res.append(curr)
                    res.extend(intervals[i + 1:])
                    break

                # overlapping with prev
                elif res and curr[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], curr[1])
                    # print("first", res)

                # overlapping with new
                elif new_start <= curr[1]:
                    res.append([min(new_start, curr[0]), max(new_end, curr[1])])
                    # print("second", res)
                else:
                    res.append(curr)

        return res


"""
insert at front
    ==      ====
==

insert at end
==      ====
                ==

overlap => build, insert combined
==      ====
 ====

overlap btw curr and new => insert combined => cmp curr with prev => extend prev
==      ====
 ========

overlap => builder => insert
==      ====
     ====

no overlap => insert builder
==      ====
    ==

"""