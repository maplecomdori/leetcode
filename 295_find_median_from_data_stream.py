class MedianFinder:

    def __init__(self):
        self.min_heap = []  # put larger numbers
        self.max_heap = []  # put smaller numbers

    def addNum(self, num: int) -> None:
        # determine which heap to add the number to
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.max_heap, -num)
        else:
            if num > self.max_heap[0] * -1:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

                # rebalance
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1)
        elif len(self.max_heap) + 1 < len(self.min_heap):
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2

"""
[1] []
[1] [2]
1.5
[1] [2,3]
2
"""