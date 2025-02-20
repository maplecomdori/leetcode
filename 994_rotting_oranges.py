class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS from each rotten orange
        # add all the rotten oranges to the queue
        # convert fresh to rotten
        # if there is a still fresh orange after BFS, return -1
        # else return minutes
        ROWS = len(grid)
        COLS = len(grid[0])
        FRESH = 1
        ROTTEN = 2
        total_fresh = 0
        queue = deque()
        visited = set()
        n_orange = 0
        for i in range(ROWS):
            for j in range(COLS):
                val = grid[i][j]
                if val == FRESH:
                    total_fresh += 1
                    n_orange += 1
                elif val == ROTTEN:
                    queue.append((i, j))
                    visited.add((i, j))
                    n_orange += 1

        if total_fresh == 0:
            return 0

        n_minute = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n_rotten = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                n_rotten += 1
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == FRESH:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

            n_minute += 1

        if n_orange == n_rotten:
            return n_minute - 1
        else:
            return -1

"""
2   1   1
0   1   1
1   0   1

2   2   1
0   1   1
1   0   1

"""