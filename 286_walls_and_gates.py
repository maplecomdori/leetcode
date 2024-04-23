class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        GATE = 0
        WALL = -1
        ROWS = len(rooms)
        COLS = len(rooms[0])

        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == GATE:
                    q.append((row, col))

        # bfs
        distance = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and rooms[new_row][new_col] == EMPTY:
                        rooms[new_row][new_col] = distance
                        q.append((new_row, new_col))

            distance += 1
