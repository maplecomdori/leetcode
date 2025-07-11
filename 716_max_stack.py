
# SortedList solution
from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()  # sorted by value (tree)
        self.count = 0

    def push(self, x: int) -> None:
        self.stack.add((self.count, x))
        self.values.add((x, self.count))
        self.count += 1

    def pop(self) -> int:
        cnt, val = self.stack.pop()
        self.values.remove((val, cnt))
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val, cnt = self.values.pop()
        self.stack.remove((cnt, val))
        return val


# stack and heap solution
class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []  # max_heap [ (-val, id) ]
        self.visited = set()  # {id}
        self.count = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.count))
        self.stack.append((x, self.count))
        self.count += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.visited:
            self.stack.pop()
        val, idx = self.stack.pop()
        self.visited.add(idx)
        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.visited:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.visited:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.visited:
            heapq.heappop(self.heap)
        neg_val, neg_id = heapq.heappop(self.heap)
        self.visited.add(-neg_id)
        return -neg_val


"""
5   1   5   [5, 1, 5], [5, 5, 5]
pop
5   1
pomax
1

5   2   3   8   1   [5,2,3,8,1] [-8, -5, -3, -2, -1]


"""
