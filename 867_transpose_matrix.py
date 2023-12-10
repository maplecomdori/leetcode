class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for col in range(COLS):
            lst = []
            for row in range(ROWS):
                lst.append(matrix[row][col])
            res.append(lst)
        return res