class Solution:

    def __init__(self, nums: List[int]):
        self.store = defaultdict(list)  # {number : [index] }
        for i, n in enumerate(nums):
            self.store[n].append(i)

    def pick(self, target: int) -> int:
        random_number = random.random()
        lst = self.store[target]
        return lst[int(random_number * len(lst))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)