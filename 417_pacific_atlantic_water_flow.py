class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        set_pacific = set()
        set_atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        for row in range(ROWS):
            set_pacific.add((row, 0))
            set_atlantic.add((row, COLS - 1))
        for col in range(COLS):
            set_pacific.add((0, col))
            set_atlantic.add((ROWS-1, col))

        # find cells reachable from the pacific
        q = deque(set_pacific)
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                visited.add((row, col))
                for dx, dy in directions:
                    new_row = row + dy
                    new_col = col + dx
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[row][col]:
                        q.append((new_row, new_col))
                        set_pacific.add((new_row, new_col))

        # find cells reachable from the pacific
        q = deque(set_atlantic)
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                visited.add((row, col))
                for dx, dy in directions:
                    new_row = row + dy
                    new_col = col + dx
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[row][col]:
                        q.append((new_row, new_col))
                        set_atlantic.add((new_row, new_col))
        return set_pacific.intersection(set_atlantic)