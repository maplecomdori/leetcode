class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        # print(max_heap)
        total = 0
        while k > 0:
            score = -1 * heapq.heappop(max_heap)
            total += score

            rem = math.ceil(score / 3)

            heapq.heappush(max_heap, -rem)
            k -= 1

        return total