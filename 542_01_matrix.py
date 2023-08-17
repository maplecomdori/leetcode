class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS solution: start from all the zeros, mark distance for all the cells at the same distance away from the closest zero.
        ROWS = len(mat)
        COLS = len(mat[0])
        visited = [[0] * COLS for _ in range(ROWS)]
        res = [[-1] * COLS for _ in range(ROWS)]

        q = deque()
        # initially add all coordinates of zero to the queue
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    visited[row][col] = 1
                    q.append((row, col))

        dist = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # perform bfs
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                res[row][col] = dist

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and not visited[new_row][new_col]:
                        visited[new_row][new_col] = 1
                        q.append((new_row, new_col))
            dist += 1

        return res

