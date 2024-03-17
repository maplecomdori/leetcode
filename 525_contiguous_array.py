class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: [0, -1]}  # {prefix_sum: length, position}
        max_val = 0
        total = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1

            if total in dic:
                length = i - dic[total][1] + dic[total][0]
                max_val = max(max_val, length)
                dic[total][0] = length
                dic[total][1] = i
            else:
                dic[total] = [0, i]

        return max_val
