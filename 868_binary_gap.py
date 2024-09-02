class Solution:
    def binaryGap(self, n: int) -> int:
        bin_str = bin(n)[2:]
        max_len = 0
        left = 0

        for right in range(1, len(bin_str)):
            if bin_str[right] == "1":
                max_len = max(max_len, right - left)
                left = right

        return max_len