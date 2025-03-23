class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.parent = [i for i in range(size)]
        self.islands = 0

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            # in the same island
            return False

        # x, y are two different islands, merge
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.parent[x] = y
            self.rank[y] += self.rank[x]

        self.islands -= 1
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        # no neighboring island => new island
        # try merging with neighboring island, no new island
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]

        def get_id(row, col):
            return row * n + col

        res = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for row, col in positions:
            if grid[row][col] == 1:
                # already marked as an island before
                res.append(uf.islands)
                continue

            uf.islands += 1
            grid[row][col] = 1

            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    uf.union(get_id(row, col), get_id(new_row, new_col))
            res.append(uf.islands)

        return res


"""
1 0 0
0 0 0
0 0 0

1 1 0   add to an existing island
0 0 0
0 0 0

1 1 0
0 0 1   a new island
0 0 0

1 1 0
0 0 1
0 1 0

1 1 1   combine two island into 1
0 0 1
0 1 0

1 1 1  
0 1 1
0 1 0

0 1 0   0 1 0
1 0 1 =>1 1 1  combine 4 island into 1
0 1 0   0 1 0
"""