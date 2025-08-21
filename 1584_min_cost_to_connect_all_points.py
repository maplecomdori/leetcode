class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # build adj_lst
        adj_lst = defaultdict(list)  # {src: [(distance, destination)]}
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                man_dist = abs(x1 - x2) + abs(y1 - y2)

                adj_lst[i].append((man_dist, j))
                adj_lst[j].append((man_dist, i))

        # build MST
        res = 0
        min_heap = [(0, 0)]  # [(dist, point)]
        visited = set()

        while len(visited) < len(points):  # stop after visiting all points
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                # skip visited node
                continue
            res += dist
            visited.add(node)
            for dest_dist, dest in adj_lst[node]:
                if dest not in visited:
                    heapq.heappush(min_heap, (dest_dist, dest))
        return res

