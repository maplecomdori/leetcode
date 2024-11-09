class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # last digit: add 1
        total = digits[-1] + 1
        carry = total // 10
        total %= 10
        digits[-1] = total

        # rest of the digit: take care of carry
        for i in range(len(digits) - 2, -1, -1):
            if carry == 0:
                break

            new = digits[i] + carry
            if new >= 10:
                carry = 1
                new %= 10
            else:
                carry = 0

            digits[i] = new

        if carry == 1:
            digits.insert(0, 1)

        return digits


"""
1   2   9
        1
=========
        digit = 0, carry = 1
    digit=2+1, carry = 0
digit=1+0, carry = 0

9   9
    1
total = 10 => 0, carry = 1
9 + 1 = 10 => 0, carry = 1

carry = 1 => insert 1 at the front
"""