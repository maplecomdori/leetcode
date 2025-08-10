class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # build adjacency list
        adj_lst = defaultdict(set)  # { src: (dest, travel_time) }
        for src, dest, travel_time in times:
            adj_lst[src].add((dest, travel_time))

        # run Dijkstra's algorithm
        visited = set()  # { node }
        min_heap = []  # [ (earliest_start_time, node) ]
        min_heap.append((0, k))
        max_time = 0

        while min_heap:
            earliest_start_time, node = heapq.heappop(min_heap)
            if node in visited:
                # this node has been already visited/processed at an earlier time
                continue
            visited.add(node)

            max_time = max(max_time, earliest_start_time)

            for nei, travel_time in adj_lst[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (earliest_start_time + travel_time, nei))

        if len(visited) == n:
            return max_time
        return -1
