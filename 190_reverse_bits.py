class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            bit = (n & 1) << i
            res = res | bit
            n >>= 1
        return res