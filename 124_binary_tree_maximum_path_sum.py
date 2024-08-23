# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float("-inf")

        def rec(node):
            if not node:
                return 0

            total = node.val

            left = max(rec(node.left), 0)  # discard subtree with negative sum
            right = max(rec(node.right), 0)

            nonlocal max_val
            # compare the sum rooted at this node including both left and right
            max_val = max(max_val, total + left + right)

            # return one path
            return node.val + max(left, right)

        rec(root)
        return max_val