# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []  # min_heap: [ (val, list_idx) ]

        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, [node.val, i])

        dummy = ListNode()
        curr = dummy

        while heap:

            val, list_idx = heapq.heappop(heap)
            node = lists[list_idx]

            curr.next = node
            curr = curr.next

            node = node.next
            lists[list_idx] = node
            if node:
                heapq.heappush(heap, [node.val, list_idx])

        return dummy.next