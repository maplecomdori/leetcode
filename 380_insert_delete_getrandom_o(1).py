class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}  # { value: index }

    def insert(self, val: int) -> bool:
        # insert if not present, return True

        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # remove if present, return True
        # find the index of the value removed, switch with the last in the list
        if val not in self.map:
            return False

        idx = self.map[val]
        last_idx = len(self.list) - 1
        last_val = self.list[-1]

        self.list[idx], self.list[last_idx] = self.list[last_idx], self.list[idx]
        self.map[last_val] = idx

        self.list.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        # each element has the same probability of being selected
        random_number = random.random()
        idx = int(len(self.list) * random_number)
        return self.list[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()