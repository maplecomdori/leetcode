# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def rec(node, running_sum):
            running_sum *= 10
            running_sum += node.val
            if not node.left and not node.right:
                return running_sum
            total = 0
            if node.left:
                total += rec(node.left, running_sum)
            if node.right:
                total += rec(node.right, running_sum)

            return total

        return rec(root, 0)