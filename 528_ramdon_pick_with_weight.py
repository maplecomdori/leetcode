class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.cum_prob = []
        prefix_sum = 0
        for n in w:
            probability = n / total + prefix_sum
            self.cum_prob.append(probability)
            prefix_sum = probability
        print(self.cum_prob)

    def pickIndex(self) -> int:
        prob = random.random()

        # linear search
        # for i in range(len(self.cum_prob)):
        #     if prob < self.cum_prob[i]:
        #         return i

        # binary search: find the cumulative probability that is less
        left = 0
        right = len(self.cum_prob) - 1

        while left < right:
            mid = (left + right) // 2

            if prob > self.cum_prob[mid]:
                left = mid + 1
            else:
                right = mid

        return left


"""
[0.1  0.2  0.4   0.8    1]
"""

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()