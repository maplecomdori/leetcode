# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # count the total number of nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # determine how many nodes are required for each sublist
        size = count // k
        size_lst = [size] * k
        rem = count % k
        idx = 0
        while idx < rem:
            size_lst[idx] += 1
            idx += 1

        # generate each sublist
        output = [None] * k
        curr = head
        for idx, size in enumerate(size_lst):
            output[idx] = curr
            prev = None
            for _ in range(size):
                prev = curr
                curr = curr.next
            if prev:
                prev.next = None

        return output
