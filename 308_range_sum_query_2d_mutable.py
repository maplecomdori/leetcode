class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # convert matrix into prefix sum for each row

        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] += matrix[row][col - 1]

        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        # update all values come right and below [row][col]
        old = self.matrix[row][col]
        if col != 0:
            old = self.matrix[row][col] - self.matrix[row][col - 1]
        diff = val - old

        for j in range(col, len(self.matrix[0])):
            self.matrix[row][j] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = 0
        for i in range(row1, row2 + 1):
            total += self.matrix[i][col2]
            if col1 > 0:
                total -= self.matrix[i][col1 - 1]

        return total

