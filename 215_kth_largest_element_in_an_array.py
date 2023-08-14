class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # count the frequency of each number, put the tuple (number, count) into max heap, pop until k <= 0
        d = Counter(nums)
        h = []
        for n, freq in d.items():
            heapq.heappush(h, (-n, freq))

        while h:
            n, freq = heapq.heappop(h)
            k -= freq
            if k <= 0:
                return n * -1

        # sort the array and choose the kth element from the end
        # nums.sort()
        # return nums[-k]