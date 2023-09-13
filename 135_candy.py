class Solution:
    def candy(self, ratings: List[int]) -> int:
        # for each rating, find the number of consecutively increasing range ending at the current rating from both left and right, find the max of the two, add them up and return the sum

        left = [1] * len(ratings)
        right = [1] * len(ratings)

        for i in range(1, len(ratings)):
            # count how many elements that are left of the current element and have less ratings than current element
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            # count how many elements that are right of the current element and have less ratings than current element
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        total = 0
        for i in range(len(ratings)):
            total += max(left[i], right[i])
        return total
