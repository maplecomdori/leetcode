class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix) - 1
        # pick a number on a side, move to the next side one by one
        while start < end:
            for i in range(end - start):
                # Save top-left
                temp = matrix[start][start + i]

                # Move bottom-left to top-left
                matrix[start][start + i] = matrix[end - i][start]

                # Move bottom-right to bottom-left
                matrix[end - i][start] = matrix[end][end - i]

                # Move top-right to bottom-right
                matrix[end][end - i] = matrix[start + i][end]

                # Move top-left (temp) to top-right
                matrix[start + i][end] = temp

            start += 1
            end -= 1
