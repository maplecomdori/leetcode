# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        old_new = {}  # old_node: new_node

        def rec(node):
            if not node:
                return

            if node in old_new:
                copy = old_new[node]
            else:
                copy = NodeCopy(val=node.val)

            if node not in old_new:
                old_new[node] = copy

            copy.left = rec(node.left)
            copy.right = rec(node.right)
            if node.random:
                if node.random not in old_new:
                    old_new[node.random] = NodeCopy(val=node.random.val)
                copy.random = old_new[node.random]

            return copy

        return rec(root)
