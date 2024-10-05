class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.moving_sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.moving_sum += val
        if len(self.queue) > self.size:
            self.moving_sum -= self.queue.popleft()

        return self.moving_sum / len(self.queue)
