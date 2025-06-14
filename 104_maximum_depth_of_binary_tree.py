# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return 0

            return 1 + max(rec(node.left), rec(node.right))

        return rec(root)

        # iterative solution
        if not root:
            return 0
        queue = deque()
        depth = 0
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                pop = queue.popleft()
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            depth += 1

        return depth