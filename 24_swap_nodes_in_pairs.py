# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            nxt = curr.next
            nxt_nxt = nxt.next

            prev.next = nxt
            nxt.next = curr
            curr.next = nxt_nxt

            prev = curr
            curr = nxt_nxt

        return dummy.next
