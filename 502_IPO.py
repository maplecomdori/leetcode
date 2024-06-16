class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # pick a project with most profit and requires less than current capital in hand

        n = len(profits)
        total = w
        max_heap = [(-profits[i], capital[i]) for i in range(n)]
        heapq.heapify(max_heap)

        while k > 0:
            lst_unaffordable = []
            while max_heap and max_heap[0][1] > total:
                tup = heapq.heappop(max_heap)
                lst_unaffordable.append(tup)

            if not max_heap:
                return total
            negative_profit, _ = heapq.heappop(max_heap)
            total -= negative_profit

            for tup in lst_unaffordable:
                heapq.heappush(max_heap, tup)

            k -= 1

        return total