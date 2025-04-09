# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def rec(pre_order, in_order):
            if not pre_order:
                return
                # find root
            root_val = pre_order[0]
            root = TreeNode(root_val)

            root_idx = in_order.index(root_val)
            # find left subtree
            left_inorder = in_order[:root_idx]
            left_preorder = pre_order[1:root_idx + 1]

            # find right subtree
            right_inorder = in_order[root_idx + 1:]
            right_preorder = pre_order[root_idx + 1:]

            left = rec(left_preorder, left_inorder)
            right = rec(right_preorder, right_inorder)

            root.left = left
            root.right = right

            return root

        return rec(preorder, inorder)


"""
3   9   20  15  7 (preorder)
9   3  15  20  7 (inorder)

root: 3
left-subtree: 9
right-subtree: 15 20 7




"""