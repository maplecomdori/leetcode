# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # count the length of the list
        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        # divide the two halves
        half = length // 2
        first = []
        second = []
        curr = head
        for i in range(length):
            if i < half:
                first.append(curr)
            else:
                second.append(curr)
            nxt = curr.next
            curr = nxt

        # merge
        answer = ListNode()
        curr = answer
        ptr1 = 0
        ptr2 = len(second) - 1

        while ptr1 < len(first):
            curr.next = first[ptr1]
            curr.next.next = second[ptr2]
            curr = curr.next.next
            curr.next = None
            ptr1 += 1
            ptr2 -= 1

        # odd length => last one saved in the second half, attach at the end
        if ptr2 >= 0:
            curr.next = second[ptr2]
            curr.next.next = None

        return answer.next