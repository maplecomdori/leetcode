class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # count solution

        # count parentheses that were not closed, left over ( or )
        open_count = 0
        close_count = 0

        for elem in s:
            if elem == '(':
                open_count += 1
            elif elem == ')':
                close_count += 1
                if open_count > 0:
                    open_count -= 1
                    close_count -= 1

        return open_count + close_count

        # stack solution
        stack = []

        for elem in s:
            if elem == '(':
                stack.append(elem)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(elem)

        return len(stack)


"""
'' 0
( 1
) 1
)) 2
(() 1
(())) => 1
())( => 2
"""