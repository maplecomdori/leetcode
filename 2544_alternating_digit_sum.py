class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        is_positive = True
        str_n = str(n)

        for c in str_n:
            if is_positive:
                total += int(c)
            else:
                total -= int(c)
            is_positive = not is_positive

        return total