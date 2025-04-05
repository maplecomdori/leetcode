class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def rec(row, col):
            if (row, col) in visited:
                return 0
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == 0:
                return 1
            visited.add((row, col))

            top = rec(row - 1, col)
            right = rec(row, col + 1)
            bottom = rec(row + 1, col)
            left = rec(row, col - 1)

            total = top + right + bottom + left
            return total

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    return rec(row, col)
