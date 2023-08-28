class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        # move everything to the second queue
        while len(self.first) > 1:
            pop = self.first.popleft()
            self.second.append(pop)
        last = self.first.popleft()
        self.first = self.second
        self.second = deque()
        return last

    def top(self) -> int:
        # move everything except the last element in the first queue to the secnod queue
        while len(self.first) > 1:
            pop = self.first.popleft()
            self.second.append(pop)
        return self.first[0]

    def empty(self) -> bool:
        return len(self.first) == 0
