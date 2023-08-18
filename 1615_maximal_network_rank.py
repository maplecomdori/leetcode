class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        # build adjacency list
        adj_lst = {}
        for src, dest in roads:
            if src not in adj_lst:
                adj_lst[src] = [dest]
            else:
                adj_lst[src].append(dest)
            if dest not in adj_lst:
                adj_lst[dest] = [src]
            else:
                adj_lst[dest].append(src)

        # check ranks for every pair
        max_val = 0
        for i in range(n-1):
            if i not in adj_lst:
                # i has no neighbor
                continue
            for j in range(i+1, n):
                if j not in adj_lst:
                    # j has no neighbor
                    continue
                if i in adj_lst[j]:
                    # account for double counting of the edge between i and j
                    max_val = max(max_val, len(adj_lst[i]) + len(adj_lst[j]) - 1)
                else:
                    max_val = max(max_val, len(adj_lst[i]) + len(adj_lst[j]))
        return max_val
