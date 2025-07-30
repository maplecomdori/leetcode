class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        res = []

        while p1 >= 0 or p2 >= 0:
            n1 = 0
            n2 = 0

            if p1 >= 0:
                n1 = ord(num1[p1]) - ord("0")
                p1 -= 1

            if p2 >= 0:
                n2 = ord(num2[p2]) - ord("0")
                p2 -= 1

            total = carry + n1 + n2
            carry = total // 10
            total %= 10
            res.append(str(total))
        if carry:
            res.append("1")
        res.reverse()
        return "".join(res)
