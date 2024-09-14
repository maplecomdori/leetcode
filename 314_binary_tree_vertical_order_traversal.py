# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        dd = defaultdict(dict)  # {col: {row: []}}

        def rec(node, row, col):
            if not node:
                return

            if row not in dd[col]:
                dd[col][row] = [node.val]
            else:
                dd[col][row].append(node.val)

            rec(node.left, row + 1, col - 1)
            rec(node.right, row + 1, col + 1)

        rec(root, 0, 0)

        res = []

        for col_num in sorted(dd.keys()):
            col_dict = dd[col_num]
            builder = []
            for row in sorted(col_dict.keys()):
                builder.extend(col_dict[row])
            res.append(builder)

        return res
