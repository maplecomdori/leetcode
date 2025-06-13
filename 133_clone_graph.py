"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new = {}  # {old_node: copied_node}

        if not node:  # empty graph
            return

        def rec(curr):
            copy = Node(curr.val)
            old_to_new[curr] = copy

            for nei in curr.neighbors:
                if nei in old_to_new:
                    copy.neighbors.append(old_to_new[nei])
                else:
                    nei_copy = rec(nei)
                    copy.neighbors.append(nei_copy)
            return copy

        return rec(node)

        # iterative solution
        if not node:
            return node

        node_to_copy = {}  # {old_node: new_copy}
        queue = deque()
        queue.append(node)
        node_to_copy[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in node_to_copy:
                    nei_clone = Node(nei.val)
                    node_to_copy[nei] = nei_clone

                    node_to_copy[curr].neighbors.append(nei_clone)
                    queue.append(nei)
                else:
                    nei_clone = node_to_copy[nei]
                    node_to_copy[curr].neighbors.append(nei_clone)

        return node_to_copy[node]