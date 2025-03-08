class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        COL_MIN = -1
        COL_MAX = len(matrix[0])
        ROW_MIN = -1
        ROW_MAX = len(matrix)

        row = col = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        dir_idx = RIGHT

        res = []
        while len(res) < m * n:
            res.append(matrix[row][col])
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
            if dir_idx == RIGHT and next_col == COL_MAX:
                dir_idx = DOWN
                ROW_MIN += 1
            elif dir_idx == DOWN and next_row == ROW_MAX:
                dir_idx = LEFT
                COL_MAX -= 1
            elif dir_idx == LEFT and next_col == COL_MIN:
                dir_idx = UP
                ROW_MAX -= 1
            elif dir_idx == UP and next_row == ROW_MIN:
                dir_idx = RIGHT
                COL_MIN += 1

            row += directions[dir_idx][0]
            col += directions[dir_idx][1]

        return res
