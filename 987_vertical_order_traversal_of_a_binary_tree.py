# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        store = defaultdict(dict) # {col: {row: []}}
        queue = deque()
        queue.append((0, 0, root))

        while queue:
            for _ in range(len(queue)):
                row, col, node = queue.popleft()
                if row not in store[col]:
                    store[col][row] = [node.val]
                else:
                    store[col][row].append(node.val)

                if node.left:
                    queue.append((row + 1, col - 1, node.left))
                if node.right:
                    queue.append((row + 1, col + 1, node.right))

        # build solution
        for col in sorted(store.keys()):
            builder = []
            for row in sorted(store[col].keys()):
                builder.extend(sorted(store[col][row]))
            res.append(builder)

        return res