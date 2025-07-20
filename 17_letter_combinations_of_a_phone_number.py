class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def rec(i):
            if i == len(digits):
                if builder:
                    res.append("".join(builder))
                return
            str_digit = digits[i]
            for char in num_to_char[str_digit]:
                builder.append(char)
                rec(i + 1)
                builder.pop()

        res = []
        builder = []
        rec(0)
        return res
