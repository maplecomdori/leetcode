# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def rec(node):

            # go left
            if p.val < node.val and q.val < node.val:
                return rec(node.left)

            # go right
            elif p.val > node.val and q.val > node.val:
                return rec(node.right)

            # at this point, not both values are not less or greater than the current node,
            # that means either two nodes can be found in left and right subtree separately
            # OR
            # the current node is equal to one of p,q and the other one is in the subtree,
            # so the current node must be LCA
            return node

        return rec(root)