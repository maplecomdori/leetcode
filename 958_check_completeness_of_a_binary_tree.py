# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # once you find null, everything that comes after should be null.
        # otherwise, it's not a complete binary tree
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):

                node = queue.popleft()
                if not node:
                    while queue:
                        if queue.popleft():
                            return False
                    return True
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return True