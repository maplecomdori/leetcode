class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # save all the 'O's that are reachable from the edge
        # mark all the '0's not in the list with 'X'

        set_edge = set()
        ROWS = len(board)
        COLS = len(board[0])

        for col in range(COLS):
            if board[0][col] == 'O':
                set_edge.add((0, col))
            if board[ROWS - 1][col] == 'O':
                set_edge.add((ROWS - 1, col))

        for row in range(1, ROWS - 1):
            if board[row][0] == 'O':
                set_edge.add((row, 0))
            if board[row][COLS-1] == 'O':
                set_edge.add((row, COLS - 1))

        # BFS to find all the '0's reachable from the edge
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        queue.extend(set_edge)
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in set_edge and board[new_row][new_col] == 'O':
                        set_edge.add((new_row, new_col))
                        queue.append((new_row, new_col))

        # check every spot and mark the '0's that are not in set_edge
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row, col) not in set_edge:
                    board[row][col] = 'X'
