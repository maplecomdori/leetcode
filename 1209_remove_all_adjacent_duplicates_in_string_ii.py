class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [ [letter, count] ]

        for char in s:
            if not stack:
                stack.append([char, 1])
                continue

            if char == stack[-1][0]:
                if k - 1 == stack[-1][1]:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([char, 1])

        return "".join([char * count for char, count in stack])


"""
d e e e d b b c c c b d a a
d,1
d,1 e,2 e
d,2 b,2
d2, b,2 c,2 c
d2, b,2 b
d2, d
a2
"""