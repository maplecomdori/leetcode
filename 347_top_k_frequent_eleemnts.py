class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap solution
        # count frequencies of each number
        counter = {} # {number: count}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        # put them in min_heap to pop numbers with smallest frequencies
        min_heap = []
        for number, count in counter.items():
            heapq.heappush(min_heap, (count, number))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # pop k elements from the heap
        res = [n for count, n in min_heap]
        return res

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
