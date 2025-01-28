class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        dic = {}  # { row+col: [elements]}

        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                total = row + col
                if total not in dic:
                    dic[total] = []
                dic[total].append(nums[row][col])

        key = 0
        res = []

        while key in dic:
            res.extend(dic[key])
            key += 1

        return res