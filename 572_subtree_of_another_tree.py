# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # try every node, and if the node has the same value as subRoot, compare

        def same_tree(a, b):
            if (a and not b) or (not a and b):
                return False
            elif not a and not b:
                return True

            if a.val != b.val:
                return False

            left = same_tree(a.left, b.left)
            if not left:
                return False
            right = same_tree(a.right, b.right)

            return left and right

        def rec(node):
            if not node:
                return False

            if node.val == subRoot.val and same_tree(node, subRoot):
                return True

            left = rec(node.left)
            if left:
                return left
            right = rec(node.right)

            return right

        return rec(root)
