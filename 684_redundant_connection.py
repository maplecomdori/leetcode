class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def find(node):

            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first, second):
            first = find(first)
            second = find(second)

            if first == second:
                return True

            if rank[first] > rank[second]:
                rank[first] += rank[second]
                parent[second] = parent[first]
            else:
                rank[second] += rank[first]
                parent[first] = parent[second]

        for src, dest in edges:
            if union(src, dest):
                return [src, dest]