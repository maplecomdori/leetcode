# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0

        node = head
        while node:
            count += 1
            node = node.next

        half_count = count // 2

        node = head
        while half_count > 0:
            half_count -= 1
            node = node.next

        return node
