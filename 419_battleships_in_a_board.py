class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def rec(row, col):
            if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != "X" or (row, col) in visited:
                return

            visited.add((row, col))

            rec(row + 1, col)
            rec(row - 1, col)
            rec(row, col + 1)
            rec(row, col - 1)

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and board[i][j] == "X":
                    rec(i, j)
                    count += 1
        return count