class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_common_divisor(divisor, string):
            if len(string) % len(divisor):
                return False
            repeat = len(string) // len(divisor)
            return divisor * repeat == string

        if len(str1) < len(str2):
            shorter = str1
            longer = str2
        else:
            shorter = str2
            longer = str1

        if is_common_divisor(shorter, longer):
            return shorter
        common_divisor = ""
        for i in range(len(shorter) // 2):
            substring = shorter[:i + 1]

            if is_common_divisor(substring, shorter):
                if is_common_divisor(substring, longer):
                    common_divisor = substring

        return common_divisor


"""
ABC ABC, ABC
AB AB AB,  AB AB

ABCAB   ABAB

"""