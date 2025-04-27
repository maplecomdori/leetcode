# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.p_found = False
        self.q_found = False

        def rec(node):
            if not node:
                return

            left = rec(node.left)
            right = rec(node.right)

            if node.val == p.val:
                self.p_found = True
                return node

            if node.val == q.val:
                self.q_found = True
                return node

            if left and right:
                return node
            else:
                return left or right

        res = rec(root)
        return res if self.p_found and self.q_found else None