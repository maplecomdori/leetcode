class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True

            total = 0
            while n > 0:
                digit = n % 10
                n //= 10
                total += digit ** 2

            n = total

        return False


"""
2, 4, 16, 37, 
9 + 49 = 58, 
25 + 64 = 89, 
64 + 81 = 145
1 + 16 + 25 = 42
16 + 4 = 20
2

"""