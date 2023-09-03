class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[-2][-2] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]

        return dp[0][0]


"""
        # top down
        visited = set() # {(row, col)}
        dp = {}

        def rec(row, col):
            if row == m -1 and col == n - 1:
                return 1
            if (row, col) in visited or row == m or col == n:
                return 0
            if (row, col) in dp:
                return dp[row, col]

            visited.add((row, col))
            down = rec(row + 1, col)
            right = rec(row, col + 1)
            visited.remove((row, col))

            dp[(row, col)] = down + right
            return down + right


        return rec(0, 0)
"""
