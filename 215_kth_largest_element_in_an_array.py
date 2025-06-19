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

        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for n in nums:
                if n > pivot:
                    left.append(n)
                elif n < pivot:
                    right.append(n)
                else:
                    mid.append(n)

            if k <= len(left):
                # answer should be in left
                return quick_select(left, k)
            elif len(left) + len(mid) < k:
                # answer should be in right
                return quick_select(right, k - len(left) - len(mid))
            else:
                # answer should be in mid
                return pivot

        return quick_select(nums, k)


"""
3   2   1   5   6   4, k=2
1   2   3   4   5   6 => 5

3   2   3   1   2   4   5   5   6, k=4
1   2   2   3   3   4   5   5   6 => 4

k=4, pivot=5
[6] [5 5] [3 2 3 1 2 4]
k=1, pivot=[1]
[3 2 3 2 4] [1] []
k=1, pivot=2
[3 3 4] [2 2] []
k=1 pivot=3
[4] [3 3] []
k=1 pivot=4
[] [4] []

"""