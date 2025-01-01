# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def rec(node):
            if not node:
                return

            if node.val in (p.val, q.val):
                return node
            else:
                left = rec(node.left)
                right = rec(node.right)

                if left and right:
                    return node
                elif left:
                    return left
                elif right:
                    return right
                else:
                    return None

        return rec(root)


"""
LCA can have p on the left tree and q on the right tree, vice versa
LCA can be one of p and q and left subtree or right subtree has the other
"""