# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def rec(first, second):
            if not first and not second:
                return True
            elif not first and second:
                return False
            elif first and not second:
                return False
            elif first.val == second.val:
                return rec(first.left, second.left) and rec(first.right, second.right)
            return False

        return rec(p, q)
