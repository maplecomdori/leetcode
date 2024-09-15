class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest integer whose sq value is less than 'x'
        if x == 0 or x == 1:
            return x

        left = 0
        right = x

        while left < right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            elif sq > x:
                right = mid

        return left - 1


'''

x=4
l   h   m   sq
0   2   1   1
2   2   2   4

x = 5 => 2
l   h   m   sq
0   2   1   1
2   2


x = 8 => 2
l   h   m   sq
0   4   2   4
3   4   3   9
3   3
3 - 1 => 2

'''