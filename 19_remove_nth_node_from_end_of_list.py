# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of the linked list
        node = head
        total = 0
        while node:
            node = node.next
            total += 1

        # find the node before the node to be removed
        dummy = ListNode(next=head)
        travel = total - n
        node = dummy
        while travel > 0:
            node = node.next
            travel -= 1

        node.next = node.next.next

        return dummy.next
