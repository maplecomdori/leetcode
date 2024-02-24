class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_lst = defaultdict(list)  # {src: [dest, price]}
        cost = [float("inf")] * n  # min cost to reach ith place
        cost[src] = 0

        for start, end, price in flights:
            adj_lst[start].append((end, price))

        queue = deque([(src, 0)])
        while queue and k >= 0:
            for _ in range(len(queue)):

                nxt, cost_so_far = queue.popleft()

                for nei, price in adj_lst[nxt]:
                    new_cost = price + cost_so_far
                    if new_cost < cost[nei]:
                        cost[nei] = new_cost
                        queue.append((nei, new_cost))
            k -= 1

        return cost[dst] if cost[dst] != float('inf') else - 1

