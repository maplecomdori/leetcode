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