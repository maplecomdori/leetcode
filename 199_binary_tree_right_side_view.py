# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            last = None
            for _ in range(len(q)):
                last = q.popleft()
                if last.left:
                    q.append(last.left)
                if last.right:
                    q.append(last.right)
            res.append(last.val)

        return res