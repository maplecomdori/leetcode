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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return

            # store numbers in list
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next

        def rec(start, end):
            if start > end:
                return

            mid = (start + end) // 2
            node = TreeNode(lst[mid])

            node.left = rec(start, mid - 1)
            node.right = rec(mid + 1, end)

            return node

        return rec(0, len(lst) - 1)
