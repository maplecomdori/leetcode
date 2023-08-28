class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # bottom up
        if stones[1] > 1:
            return False

        d = {v: i for i, v in enumerate(stones)}  # {stone: index}
        dp = [False] * len(stones)
        dp[0] = True
        jumps = [set() for _ in range(len(stones))]  # specific n of jumps used to reach ith stone
        jumps[0].add(1)

        for i in range(len(stones)):
            for jump in jumps[i]:
                # for each jump unit used to reach ith stone
                if jump - 1 > 0 and stones[i] + jump - 1 in d:
                    # try k-1 jumps to reach some stone
                    idx = d[stones[i] + jump - 1]
                    dp[idx] = True
                    jumps[idx].add(jump - 1)

                if stones[i] + jump in d:
                    # try k jumps to reach some stone
                    idx = d[stones[i] + jump]
                    dp[idx] = True
                    jumps[idx].add(jump)

                if i != 0 and stones[i] + jump + 1 in d:
                    # try k + 1 jumps to reach some stone
                    idx = d[stones[i] + jump + 1]
                    dp[idx] = True
                    jumps[idx].add(jump + 1)
        return dp[-1]

        # top down
        d = {v: i for i, v in enumerate(stones)}  # {stone: index}
        dp = {}

        def rec(i, k):
            if i == len(stones) - 1:
                # reached the last stone
                return True

            if (i, k) in dp:
                return dp[(i, k)]

            # jump k-1
            # can move forward, there's a stone in the next destination, and can reach the last stone
            if k - 1 > 0 and stones[i] + k - 1 in d and rec(d[stones[i] + k - 1], k - 1):
                dp[(i, k)] = True
                return True

            # jump k
            if k > 0 and stones[i] + k in d and rec(d[stones[i] + k], k):
                dp[(i, k)] = True
                return True

            # jump k + 1
            if k + 1 > 0 and stones[i] + k + 1 in d and rec(d[stones[i] + k + 1], k + 1):
                dp[(i, k)] = True
                return True

            return False

        if stones[1] > 1:
            return False

        return rec(1, 1)
