# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()  # nodes whose val < x
        dummy = ListNode(next=head)

        # go through the list and remove nodes < x from the main LL and append to the left LL
        curr = dummy
        lcurr = left

        while curr and curr.next:
            nxt = curr.next
            if nxt.val < x:
                # remove from the main LL
                curr.next = nxt.next

                # append to the left part LL
                lcurr.next = nxt
                nxt.next = None
                lcurr = lcurr.next

            else:
                curr = curr.next

        # comebine the two LL: left + dummy
        left_end = left
        while left_end.next:
            left_end = left_end.next

        left_end.next = dummy.next

        return left.next


"""
========================================================================
d   1   4   3   2   5   2
c
l   1

d   4   3   2   5   2
    c
l   1

d   4   3   2   5   2
        c
l   1   2

d   4   3   5   2
            c
l   1   2   2

d   4   3   5
l   1   2   2

========================================================================
d   1   4   3   0   2   5   2, x=3
c
l   1

d   4   3   0   2   5   2
    c
l   1

d   4   3   0   2   5   2
        c
l   1   0

d   4   3   2   5   2
        c
l   1   0   2

d   4   3   5   2
        c
l   1   0   2

d   4   3   5   2
            c
l   1   0   2   2

d   4   3   5

"""

