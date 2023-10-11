class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(first, second):
            first_parent = find(first)
            second_parent = find(second)

            if first_parent == second_parent:
                return 0
            elif rank[first_parent] > rank[second_parent]:
                rank[first_parent] += rank[second_parent]
                parent[second_parent] = first_parent
                return 1
            else:
                rank[second_parent] += rank[first_parent]
                parent[first_parent] = second_parent
                return 1

        for src, dest in edges:
            n -= union(src, dest)
        return n
