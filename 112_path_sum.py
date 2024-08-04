# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def rec(node, total):
            if not node:
                return False
            if not node.left and not node.right: # leaf
                return targetSum == total + node.val
            return rec(node.left, total + node.val) or rec(node.right, total + node.val)
        return rec(root, 0)