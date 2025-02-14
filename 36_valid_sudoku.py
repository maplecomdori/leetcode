class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # ONE PASS
        SIZE = 9
        seen_row = [set() for _ in range(SIZE)]
        seen_col = [set() for _ in range(SIZE)]
        seen_box = [[set() for _ in range(SIZE // 3)] for _ in range(SIZE // 3)]

        for row in range(SIZE):
            box_row = row // 3
            for col in range(SIZE):
                val = board[row][col]
                if val == '.':
                    continue
                box_col = col // 3

                if val in seen_row[row] or val in seen_col[col] or val in seen_box[box_row][box_col]:
                    return False
                seen_row[row].add(val)
                seen_col[col].add(val)
                seen_box[box_row][box_col].add(val)

        return True

        # BRUTE FORCE
        # check each row & col & box
        ROWS = len(board)
        COLS = len(board[0])

        # check row
        for row in range(ROWS):
            seen = set()
            for col in range(COLS):
                val = board[row][col]
                if val != '.' and val in seen:
                    return False
                else:
                    seen.add(board[row][col])

        # check col
        for col in range(COLS):
            seen = set()
            for row in range(ROWS):
                val = board[row][col]
                if val != '.' and val in seen:
                    return False
                else:
                    seen.add(board[row][col])

        # check box
        for box_row in range(3):
            row_start = box_row * 3
            for box_col in range(3):
                col_start = box_col * 3
                seen = set()
                for row_offset in range(3):
                    row = row_start + row_offset
                    for col_offset in range(3):
                        col = col_start + col_offset
                        val = board[row][col]
                        if val != '.' and val in seen:
                            return False
                        else:
                            seen.add(val)
        return True
