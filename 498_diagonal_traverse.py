class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        go_right = 1
        directions = [(1, -1), (-1, 1)]
        ROWS = len(mat)
        COLS = len(mat[0])
        row = 0
        col = 0
        res = []
        # switch directions when out of bounds
        for _ in range(ROWS * COLS):
            res.append(mat[row][col])
            dr, dc = directions[go_right]
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                row = new_row
                col = new_col
                continue

            # went out of grid
            if go_right:

                # right corner
                if new_row == -1 and new_col == COLS:
                    row += 1
                # top
                elif new_row == -1:
                    col = new_col
                # right
                elif new_col == COLS:
                    row += 1

            else:
                # left corner
                if new_row == ROWS:
                    col += 1
                # bottom
                elif new_row == ROWS:
                    col += 1
                # left
                elif new_col == -1:
                    row += 1

            go_right = not go_right
        return res


"""
1   2   5   6
3   4   7   8

1   2 
3   5
4   6
7   8
"""