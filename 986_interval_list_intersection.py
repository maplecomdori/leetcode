class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]

            if max(first[0], second[0]) <= min(first[1], second[1]):
                # intersecting
                res.append( [max(first[0], second[0]), min(first[1], second[1])] )

            # advance the pointer that ends earlier
            if first[1] < second[1]:
                i += 1
            else:
                j += 1

        return res


"""
====
  ====

  ====
====

==================
======  =======


    ===
===

===
    ===

"""

