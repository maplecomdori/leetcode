class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        xor = (a ^ b) & mask
        aand = ((a & b) << 1) & mask

        while aand:
            tmp = aand
            aand = ((aand & xor) << 1) & mask
            xor = (xor ^ tmp) & mask

        max_int = 0x7FFFFFFF
        return xor if xor < max_int else ~(xor ^ mask)


"""
1 + 2 = 3

01
10
== OR
11

2 + 3 = 5
    10
    11
    ==
   101

    10  10
    11  11
    AND XOR
    10  01
    <<
   100  01
    01
   AND
   000

   100 + 01 = 101

3 + 3 = 6
    11  11
    11  11
   AND  XOR
    11  00
    <<
   110 + 00 = 110

5 + 3 = 8
    101 101
     11  11
    AND  XOR
    001 110
    <<
    010 010
    110 110
    AND XOR
    010 100
    <<
    100 100
    100 100
    AND XOR
    100 000
    <<
   1000 000

   1000 + 000 = 1000


"""