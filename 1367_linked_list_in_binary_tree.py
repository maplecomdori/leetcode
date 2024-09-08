# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def rec(tree_node, list_node):
            # recursively check each node in the path
            if not list_node:
                return True
            elif not tree_node:
                return False

            if list_node.val == tree_node.val:
                return rec(tree_node.left, list_node.next) or rec(tree_node.right, list_node.next)
            else:
                return False

        def check_path(tn, ln):
            # check the path starting at each tree node
            if not tn:
                return False
            if rec(tn, ln):
                return True
            else:
                return check_path(tn.left, ln) or check_path(tn.right, ln)

        return check_path(root, head)