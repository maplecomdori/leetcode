class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = 1
        i = 0
        operator = "+"

        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1

                number = int(s[start:i])

                if operator == "+":
                    stack.append(number)
                elif operator == "-":
                    stack.append(number * -1)
                elif operator == "*":
                    stack[-1] *= number
                elif operator == "/":
                    ans = stack[-1] / number
                    stack[-1] = int(ans)

            else:
                operator = s[i]
                i += 1

        return sum(stack)


"""
10-10*10
[10]
[10, -10]
[10, -100]


3 + 2 * 2
[3]
[3, 2]
[3, 4] => 7

3 - 2 * 2
[3]
[3, -2]
[3, -4]


"""