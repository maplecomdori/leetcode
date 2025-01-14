class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        left, right = 0, 0
        queue = deque()  # keep the indices for 0

        while right < len(nums):
            n = nums[right]
            if n == 1:
                max_len = max(max_len, right - left + 1)
                right += 1

            else:
                queue.append(right)
                if k > 0:
                    k -= 1
                    max_len = max(max_len, right - left + 1)
                    right += 1
                else:
                    last_zero_index = queue.popleft()
                    left = last_zero_index + 1
                    right += 1

        return max_len


"""
1   1   1   0   0   0   1   1   1   1   0,  k
lr                                          2
l       r                                   2
l           r                               1
l               r                           0
l                   r
                l   r                       1
                l   r                       0
                l       r
                l                   r

0   0   1   1   0   0   1   1   1   0   1   1   0   0   0   1   1   1   1, k=3
l               r
    l               r
        l                           r

"""