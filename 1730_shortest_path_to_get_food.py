class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        start = None
        # find start point
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '*':
                    start = (i, j)
                    break

        # run bfs
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        steps = 0
        while q:

            for _ in range(len(q)):
                spot = q.popleft()
                if grid[spot[0]][spot[1]] == '#':
                    return steps
                for dx, dy in directions:
                    new_row = spot[0] + dx
                    new_col = spot[1] + dy

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and \
                            grid[new_row][new_col] in {'#', 'O'}:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
            steps += 1

        return -1