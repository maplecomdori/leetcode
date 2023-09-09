class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows >= 2:
            res.append([1, 1])

        for i in range(3, numRows + 1):
            lst = [1]
            last_lst = res[-1]
            for j in range(i - 2):
                lst.append(last_lst[j] + last_lst[j + 1])

            lst.append(1)
            res.append(lst)

        return res
