"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        curr = head.next
        nxt = curr.next
        node = Node(val=insertVal)

        while curr != head:
            if curr.val > nxt.val and (insertVal <= nxt.val or insertVal >= curr.val):
                # insert a new min / max between the curr max and min where curr.val > nxt.val
                node.next = nxt
                curr.next = node
                return head
            elif curr.val <= insertVal < nxt.val:
                # insert between two existing node
                curr.next = node
                node.next = nxt
                return head
            else:
                curr = nxt
                nxt = nxt.next

        # insert after head
        node.next = nxt
        head.next = node
        return head

"""
3   4   1, insert 5 => between 1 and 4      insert at the max
3   4   1, insert 0 => between 1 and 4      insert at the min
3   4   1, insert 3 => insert at head.next
2   2   2, insert 3
2   2   2, insert 1


head => 1, insert 0
head => 1 => 0
"""