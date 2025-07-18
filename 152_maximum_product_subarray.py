class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = 1
        min_so_far = 1
        max_val = nums[0]

        for curr in nums:
            tmp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = tmp_max
            max_val = max(max_val, max_so_far)

        return max_val


"""
case 1, two positive numbers
2   3   arr
2   6   max <= from curr * max
2   3   neg
case 2, neg & pos
-2  3   arr
-2  3   max <= from curr
-2  -6  min
case 3, pos & neg
2   -3  arr
2   -3  max <= from curr
2   -6  min

case 4, neg & neg
-2  -3  arr
-2  6   max <= min * curr
-2  -3  min <= curr

case 5, neg & pos & neg
-2  3   -2
-2  3   12  max <= from curr * min
-2  -6  -6  min


2   3   -2  4
2
    6
        -12
            -48
    3   -6  -24
        -2  -8
            4

2   6   -2  4
2   3   -12 -48

-2  0   -1
-2  0   0
    0   0
        -1

-2  0   0   curr_max
-2  0   -1  curr_min

0   0   0

-2  -3  -4
-2  6   -24
    -3  12
        -4

-2  6   12      curr_max
-2  -3  -24     curr_min

"""