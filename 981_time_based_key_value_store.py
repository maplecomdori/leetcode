class TimeMap:

    def __init__(self):
        self.store = {}  # {key: [(val, time)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        lst = self.store[key]
        # find the first timestamp that is <= the given timestamp
        # for i in range(len(lst) - 1, -1, -1):
        #     ts = lst[i][1]
        #     if ts <= timestamp:
        #         return lst[i][0]
        # return ""

        # binary search
        left = 0
        right = len(lst) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            ts = lst[mid][1]

            if ts <= timestamp:
                res = lst[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


"""
foo: (bar, 1)
get("foo", 1) => bar
get("foo", 3) => bar
foo: (bar, 1) (bar2, 4)
get("foo", 4) => bar2'
get("foo", 5) => bar2
"""
