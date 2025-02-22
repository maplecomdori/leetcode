# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def rec(node):
            if not node:
                return True, 0

            left_balanced, left_height = rec(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_height = rec(node.right)
            if not right_balanced:
                return False, 0

            return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

        tree_balanced, tree_height = rec(root)
        return tree_balanced

        # res = True

        # def rec(node):
        #     if not node:
        #         return 0

        #     left_height = rec(node.left)
        #     right_height = rec(node.right)

        #     if abs(left_height - right_height) > 1:
        #         nonlocal res
        #         res = False

        #     return max(left_height, right_height) + 1

        # rec(root)
        # return res
