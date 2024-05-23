class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def rec(row, col):
            if not 0 <= row < ROWS or not 0 <= col < COLS or (row, col) in visited or grid[row][col] == "0":
                return

            visited.add((row, col))
            rec(row - 1, col)
            rec(row + 1, col)
            rec(row, col + 1)
            rec(row, col - 1)

        total = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    rec(i, j)
                    total += 1

        return total
