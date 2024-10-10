class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # one row => no need to check
        if ROWS == 1:
            return True

        # for every column in the first row => go right bottom
        for start_col in range(COLS):
            # go through the diagonal
            row = 0
            col = start_col
            while row + 1 < ROWS and col + 1 < COLS:
                # print(row, col)
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
                row += 1
                col += 1

        # for every row from second row, go right bottom
        for start_row in range(1, ROWS):
            row = start_row
            col = 0
            while row + 1 < ROWS and col + 1 < COLS:
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
                row += 1
                col += 1

        return True