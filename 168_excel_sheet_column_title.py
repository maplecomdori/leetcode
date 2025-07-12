class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        lst = []
        while n > 0:
            rem = n % 26
            if rem == 0:
                lst.append("Z")
                n -= 1
            else:
                c = chr(ord("A") - 1 + rem)
                lst.append(c)
            n //= 26
        lst.reverse()
        return "".join(lst)
