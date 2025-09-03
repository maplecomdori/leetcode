class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        min_heap = []  # [ (val, row, col) ]
        ROWS = len(grid) - 1
        COLS = len(grid[0]) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited.add((0, 0))
        min_heap.append((grid[0][0], 0, 0))

        while min_heap:
            val, row, col = heapq.heappop(min_heap)

            if row == ROWS and col == COLS:
                return val

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row <= ROWS and 0 <= new_col <= COLS and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    heapq.heappush(min_heap, (max(val, grid[new_row][new_col]), new_row, new_col))

        return -1