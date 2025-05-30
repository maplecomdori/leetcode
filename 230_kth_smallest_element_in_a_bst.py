# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # inorder traversal
        res = []

        def rec(node):
            if not node:
                return

            rec(node.left)
            res.append(node.val)
            rec(node.right)

        rec(root)
        return res[k - 1]

        # iterative
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right