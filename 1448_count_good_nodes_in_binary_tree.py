# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def rec(node, cur_max):
            if not node:
                return 0

            if node.val < cur_max:
                return rec(node.left, cur_max) + rec(node.right, cur_max)
            else:
                return 1 + rec(node.left, node.val) + rec(node.right, node.val)

        return rec(root, -10 ** 5)