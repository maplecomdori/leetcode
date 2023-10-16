class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        last = [1, 1]

        while rowIndex > 1:
            curr = [1]
            for i in range(len(last) - 1):
                curr.append(last[i] + last[i + 1])

            curr.append(1)
            last = curr
            rowIndex -= 1

        return last


"""
0 [1]
1 [1,1]
2 [1, 2, 1]
3 [1, 3, 3, 1]
4 [1, 4, 6, 4, 1]

"""