class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def rec(row, col, i):
            if i == len(word):
                return True

            if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != word[i] or (row, col) in visited:
                return False

            visited.add((row, col))
            up = rec(row - 1, col, i + 1)
            down = rec(row + 1, col, i + 1)
            right = rec(row, col + 1, i + 1)
            left = rec(row, col - 1, i + 1)
            visited.remove((row, col))
            return up or down or right or left

        for i in range(ROWS):
            for j in range(COLS):
                if rec(i, j, 0):
                    return True

        return False