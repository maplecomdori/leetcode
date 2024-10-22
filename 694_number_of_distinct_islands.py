class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()  # { (row, col) }

        def rec(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == 0 or (row, col) in visited:
                return

            visited.add((row, col))
            builder.append(str(row - row_origin) + '-' + str(col - col_origin))

            rec(row, col + 1)
            rec(row + 1, col)
            rec(row - 1, col)
            rec(row, col - 1)

        set_island = set()
        for i in range(ROWS):
            for j in range(COLS):
                builder = []  # [ 'row-col' ]
                row_origin = i
                col_origin = j
                rec(i, j)
                if builder:
                    key = ",".join(builder)
                    set_island.add(key)

        return len(set_island)


"""
save the island into a list of coordinates
11
11 => (0,0) (0,1) (1,0) (1,1)

11
11 => (2,3) (2,4) (3,3) (3,4)
        convert as if starts from 0,0 by subtracting the left most

take the lowest row number and take the lowest col number to 0
 1
111

"""