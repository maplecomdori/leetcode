class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def bfs(row, col):
            area = 0
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    area += 1

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j)
                    max_area = max(max_area, area)

        return max_area