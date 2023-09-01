class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]

        # copy the existing elements in dp and append after + 1
        while len(dp) <= n:
            for i in range(len(dp)):
                dp.append(dp[i] + 1)
                if len(dp) == n + 1:
                    return dp

        return dp
"""a
0 --> 0     0

1 --> 1     1

2 --> 10    1
3 --> 11    2

4 --> 100   1
5 --> 101   2
6 --> 110   2
7 --> 111   3

8 --> 1000  1
9 --> 1001  2
10 --> 1010 2 
11 --> 1011 3
12 --> 1100 2  
13 --> 1101 3
14 --> 1110 3
15 --> 1111 4

16 --> 10000  1
"""