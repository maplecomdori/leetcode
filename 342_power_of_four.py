class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # bit manipulation solution
        if n <= 0:
            return False

        # count bits at 1,4,16,64..
        count_4 = 0
        # count bits at 2,8,32...
        count_rest = 0

        while n > 0:
            count_4 += n & 1
            n = n >> 1
            count_rest += n & 1
            n = n >> 1

        return count_4 == 1 and count_rest == 0

        # loop solution
        if n <= 0:
            return False

        while True:
            if n == 1:
                return True

            if n % 4 != 0:
                return False
            n //= 4


"""
0   0   0   0   0   0   0
64  32  16  8   4   2   1

16
4
1

5 => False

1 => True

0 => False

-1 => False
-16=> False
"""