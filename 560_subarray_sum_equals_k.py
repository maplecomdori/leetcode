class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum_freq = defaultdict(int)  # { sum: freq }
        sum_freq[0] = 1
        prefix_sum = 0

        for n in nums:
            prefix_sum += n
            diff = prefix_sum - k

            if diff in sum_freq:
                res += sum_freq[diff]

            sum_freq[prefix_sum] += 1

        return res

"""
1   1   1,  k=2 => 2        sum_frequencies:    res
1                           1:1
1   2                       1:1 2:1             1
1   2   3                   1:1 2:1 3:1         2


0   0   0, k=0 => 6         sum_freq        res
1                           0:1             
    2                       0:2
        3                   0:3


1   -1  1   1   1   1 k=3  sum_freq             res
1                           0:1, 1:1
    0                       0:2 1:1
        1                   0:2 1:2
            2               0:2 1:2 2:1
                3           0:2 1:2 2:1 3:1     2 (prefix_sum-k which is 0 has appeared before )
                    4                           4 (4 - 3) appeared twice before
=====


"""