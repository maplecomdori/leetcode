class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # sum each row's total, order by the sum, return first k indices
        lst = [(sum(mat[i]), i) for i in range(len(mat))]
        lst.sort()

        res = []
        for i in range(k):
            res.append(lst[i][1])
        return res