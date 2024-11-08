class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast < 0:
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    # remove asteroids that are moving right and weighing less than current one
                    stack.pop()

                if stack and stack[-1] > 0 and stack[-1] == -ast:
                    # if the weight are the same, both explode
                    stack.pop()
                    continue

                if not stack:
                    # popped all the elements in the stack
                    stack.append(ast)
                elif stack[-1] < 0:
                    # all the elements in the stack are moving left
                    stack.append(ast)
            else:
                stack.append(ast)
        return stack