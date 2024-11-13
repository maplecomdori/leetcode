class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        i = 0
        while i < len(s):
            curr = s[i]
            if not stack or stack[-1] != curr:
                stack.append(curr)
                i += 1
                continue

            stack.pop()
            i += 1
        return "".join(stack)


"""
a   b   b   b   a   c   a => abaca


"" => ""

a   z   x   x   z   y

"""