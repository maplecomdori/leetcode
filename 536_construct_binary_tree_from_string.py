# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # iterative solution
        if not s:
            return
        stack = []
        sign = 1
        i = 0

        while i < len(s):
            char = s[i]
            if char == '-':
                sign = -1
                i += 1
            elif char.isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                number = int(s[i:j]) * sign
                node = TreeNode(number)
                stack.append(node)
                sign = 1
                i = j
            elif char == '(':
                i += 1
                continue
            elif char == ')':
                pop = stack.pop()
                top = stack[-1]
                if top.left:
                    top.right = pop
                else:
                    top.left = pop
                i += 1

        return stack[0]

        # string: number()()
        def rec(string):

            if not string:
                return

            # read number
            if string[0] == '-':
                sign = -1
                start = end = 1
            else:
                sign = 1
                start = end = 0

            while end < len(string) and string[end].isdigit():
                end += 1

            number = int(string[start:end]) * sign
            node = TreeNode(number)

            # read left subtree if exists
            if end == len(string):
                return node

            start = end
            stack = []
            stack.append(string[end])
            end += 1
            while stack:
                if string[end] == '(':
                    stack.append('(')
                    end += 1
                elif string[end] == ')':
                    stack.pop()
                    end += 1
                else:
                    end += 1

            node.left = rec(string[start + 1:end - 1])

            # read right subtree if exists
            if end == len(string):
                return node

            start = end
            stack = []
            stack.append(string[end])
            end += 1
            while stack:
                if string[end] == '(':
                    stack.append('(')
                    end += 1
                elif string[end] == ')':
                    stack.pop()
                    end += 1
                else:
                    end += 1

            node.right = rec(string[start + 1:end - 1])

            return node

        return rec(s)


"""
4   ( 2  (3) (1) )   ( 6  (5) )   

"""