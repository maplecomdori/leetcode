# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        self.closest = root.val

        node = root
        while node:
            abs_diff = abs(target - node.val)
            if abs(target - node.val) < abs(target - self.closest):
                self.closest = node.val
            elif abs(target - node.val) == abs(target - self.closest) and node.val < self.closest:
                self.closest = node.val

            if target < node.val:
                # no need to go right as diff gets larger
                node = node.left
            else:
                node = node.right

        return self.closest
