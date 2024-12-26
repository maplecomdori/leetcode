class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_id = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dic = {}  # { island_id: size }
        ROWS = len(grid)
        COLS = len(grid[0])

        # mark grid with island_id, count island size
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    queue = deque()
                    grid[row][col] = island_id
                    queue.append((row, col))
                    visited.add((row, col))
                    size = 1
                    while queue:
                        for _ in range(len(queue)):
                            r, c = queue.popleft()
                            for dr, dc in directions:
                                new_row = r + dr
                                new_col = c + dc
                                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and \
                                        grid[new_row][new_col] == 1:
                                    visited.add((new_row, new_col))
                                    queue.append((new_row, new_col))
                                    grid[new_row][new_col] = island_id
                                    size += 1

                    dic[island_id] = size
                    island_id -= 1
        # print(grid)
        # print(dic)
        # try converting each 0 to 1
        max_size = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    visited_island = set()
                    size = 1
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] != 0 and \
                                grid[new_row][new_col] not in visited_island:
                            island_id = grid[new_row][new_col]
                            size += dic[island_id]
                            visited_island.add(island_id)

                    max_size = max(max_size, size)

        # if max_size == 0, there is no 0 in the grid
        return max_size if max_size else ROWS * COLS