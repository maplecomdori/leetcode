class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2's complement: -x = ~x + 1
        # ~x + 1 keeps the rightmost 1-bit and flips all the other bits
        # if a number is power of two, it has only one bit on, so n & (-n) should be itself
        # if it's not, the number should still have
        return n > 0 and n & (-n) == n

        # (x - 1) sets the rightmost 1-bit to 0, and set all the lower bits to 1
        # x & (x-1) => rightmost 1-bit will be turned off
        # power of two will have only a single bit turned on.
        # If a number is a power of two, x & (x - 1) should be 0 because the 1 bit will be 0
        return n > 0 and n & (n - 1) == 0

        # count the number of bits, if 1 => true
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1

        return count == 1


"""
1 => 01
2 => 10
4 => 100
"""