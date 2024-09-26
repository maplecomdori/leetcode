class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        dest_row = len(grid) - 1
        dest_col = len(grid[0]) - 1
        count = 1
        queue = deque()
        queue.append((0, 0))
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        visited = set()
        visited.add((0, 0))
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == dest_row and col == dest_col:
                    return count

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row <= dest_row and 0 <= new_col <= dest_col and grid[new_row][new_col] == 0 and (
                    new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

            count += 1

        return -1