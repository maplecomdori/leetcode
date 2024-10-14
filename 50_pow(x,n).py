class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {0: 1, 1: x}
        is_pos = n > 0
        n = abs(n)

        def rec(a, power):

            if power in cache:
                return cache[power]
            if power % 2:
                res = a * rec(a, power // 2) * rec(a, power // 2)
                cache[power] = res
                return res
            else:
                res = rec(a, power // 2) * rec(a, power // 2)
                cache[power] = res
                return res

        ans = rec(x, n) if is_pos else 1 / rec(x, n)

        return ans


"""
x=2 n=10
2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
2^10
2^5 * 2^5
(2^1 * 2^2 * 2^2) * (2^1 * 2^2 * 2^2)
2^1 * [(2^1 * 2^1) * (2^1 * 2^1)]


2^-2
1 / 4

-2 ^ 3
-2 * (2 * 2) = -8
"""