class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if two integers have the same differece with x, smaller is considered closer
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1

        return arr[left:left + k]


"""
0   1   2   3   4
1   2   3   4   5, k=4, x=3
=============

=============
1   1   2   3   4   5, k=4 x=-1
l   m   r   -1-1=-2 vs 5-(-1)=6
lm  r       -1-1=-2 vs 4-(-1)=5
lr


        =============
1   2   3   4   5   6   7   8   9, k=4, x=5
l       m       r       7-5
l   m   r       5-2 vs 6-5
    l   r       5-2 vs 6-5
        lr

1   3   6, x=3, k=2

                        =========
0   1   2   3   4   5   6   7   8
1   1   2   2   2   2   2   3   3,  x=3, k=3
                                    x-arr[mid]  arr[mid+k]-x    no abs()    using abs
l           m           r           3-2=1       2-3=-1          go right    go left

"""