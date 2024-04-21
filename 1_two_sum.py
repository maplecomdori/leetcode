class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} # target - n: index
        for i, n in enumerate(nums):
            diff = target - n
            if n in dic:
                return [i, dic[n]]
            dic[diff] = i

