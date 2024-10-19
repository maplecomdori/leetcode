class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        res = []

        # add the missing range before the first element
        if len(nums) > 0 and lower < nums[0]:
            res.append([lower, nums[0] - 1])

        # add the missing range between the elements in 'nums'
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                res.append([nums[i] + 1, nums[i + 1] - 1])

        # add the missing range after the last element
        if len(nums) > 0 and nums[-1] < upper:
            res.append([nums[-1] + 1, upper])

        return res


"""
range = [0, 99]
0   1   3   50  75
i   j
    i   j           [2,2]
        i   j       [4,49]
            i   j   [51,74]
                i   [76,99]

range = [0, 99]
5   10  [0,4], [6,9], [11,99]


range = [0, 99]
90  99  [0, 90]
i       [91, 98]
    i   nothing

range = [0, 99]
0   10

range = [0, 99]
1
"""