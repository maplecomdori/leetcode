class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        builder = []

        # skip leading space
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        # determine sign
        is_negative = False
        if s[i] == "-":
            is_negative = True
            i += 1
        elif s[i] == "+":
            i += 1

        # skip leading zeros until non-digit charactor encountered or end
        while i < len(s) and s[i] == "0":
            i += 1
        while i < len(s) and s[i].isdigit():
            builder.append(s[i])
            i += 1

        # no digits => return 0
        if not builder:
            return 0

        res = int("".join(builder))
        res = -res if is_negative else res

        # rounding
        if res < -1 * (2 ** 31):
            res = -1 * (2 ** 31)
        elif res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        return res