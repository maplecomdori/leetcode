"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}  # {old: copy}

        def rec(node):
            if not node:
                return

            if node not in mapping:
                copy = Node(node.val)
                mapping[node] = copy
            else:
                copy = mapping[node]

            copy.next = rec(node.next)
            copy.random = mapping.get(node.random, None)

            return copy

        return rec(head)
