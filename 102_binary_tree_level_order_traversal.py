# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # do bfs
        q = deque()
        q.append(root)
        res = []

        while q:
            nxt = deque()
            curr_level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            q = nxt
            res.append(curr_level)

        return res
