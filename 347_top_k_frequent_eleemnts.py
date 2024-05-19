class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        lst = [[] for i in range(len(nums) + 1)]  # lst[j] contains elements that occur j times
        counter = Counter(nums)
        for n, count in counter.items():
            lst[count].append(n)

        res = []
        for i in range(len(lst) - 1, -1, -1):
            for j in range(len(lst[i]) - 1, -1, -1):
                k -= 1
                res.append(lst[i][j])
                if k == 0:
                    return res
