# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # N < LOW => go right
        # LOW < N < HIGH => go left and right
        # HIGH < N => go left

        def rec(node):
            if not node:
                return 0
            elif low <= node.val <= high:
                return node.val + rec(node.left) + rec(node.right)
            elif node.val < low:
                return rec(node.right)
            elif high < node.val:
                return rec(node.left)

        return rec(root)