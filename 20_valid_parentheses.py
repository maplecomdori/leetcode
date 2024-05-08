class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in dic:
                # open bracket
                stack.append(c)
            else:
                # closing bracket
                if stack and stack[-1] == dic[c]:
                    # found a matching opening bracket
                    stack.pop()
                else:
                    return False

        return len(stack) == 0