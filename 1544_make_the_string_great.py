class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char.isupper():
                    if stack and stack[-1] == char.lower():
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    if stack and stack[-1] == char.upper():
                        stack.pop()
                    else:
                        stack.append(char)

        return "".join(stack)
