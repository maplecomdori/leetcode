class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == '+':
                pop = stack.pop()
                stack[-1] += pop
            elif tok == '-':
                pop = stack.pop()
                stack[-1] -= pop
            elif tok == '/':
                pop = stack.pop()
                stack[-1] = int(stack[-1] / pop)
            elif tok == '*':
                pop = stack.pop()
                stack[-1] *= pop
            else:
                stack.append(int(tok))

        return stack[0]