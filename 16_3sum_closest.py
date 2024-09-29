class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        res = (nums[0] + nums[1] + nums[2])
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = abs(total - target)

                if diff < min_diff:
                    res = total
                    min_diff = diff

                if total < target:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return res


'''
-1  2   1   -4, target = 1
-4  -1  1   2
i   j       k   -3
i       j   k   -1
    i   j   k   2


-4  -1  -1  1   1   1   2
i   j                   k   -3
i       j               k
i           j           k   
    i   j               k   0
    i       j           k   2
    i       j       k       1
    i           j   k       1
        i   j           k   2
        repeat

'''