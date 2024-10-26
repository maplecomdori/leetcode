class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []  # max_heap of size k, storing (dist, x, y)

        for x, y in points:
            dist = x ** 2 + y ** 2

            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y))

                continue

            if -heap[0][0] > dist:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist, x, y))

        return [(x, y) for dist, x, y in heap]
