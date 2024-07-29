class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adj_lst
        adj_lst = defaultdict(list)
        for src, dest in edges:
            adj_lst[src].append(dest)
            adj_lst[dest].append(src)

        visited = set()

        def rec(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj_lst[node]:
                if nei != prev:
                    if not rec(nei, node):
                        return False
            return True

        return rec(0, -1) and len(visited) == n

