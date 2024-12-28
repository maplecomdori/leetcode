"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        def rec(node):
            if not node:
                return None, None

            left_leftmost_node, left_rightmost_node = rec(node.left)
            node.left = left_rightmost_node

            if left_rightmost_node:
                left_rightmost_node.right = node

            right_leftmost_node, right_rightmost_node = rec(node.right)

            node.right = right_leftmost_node

            if right_leftmost_node:
                right_leftmost_node.left = node

            leftmost_node = left_leftmost_node if left_leftmost_node else node
            rightmost_node = right_rightmost_node if right_rightmost_node else node
            return leftmost_node, rightmost_node

        leftmost, rightmost = rec(root)
        leftmost.left = rightmost
        rightmost.right = leftmost

        return leftmost


