# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def rec(node, cur_min, cur_max):
            if not node:
                return True

            if not (cur_min < node.val < cur_max):
                return False

            return rec(node.left, cur_min, node.val) and rec(node.right, node.val, cur_max)

        return rec(root, float('-inf'), float('inf'))


"""
n  min max
2 -inf inf
5   2   inf
3   2   5
1   2   3

"""