"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # O(1) space solution
        # travel up the tree for both and when it reaches null, move the pointer to the other
        # this way, both pointers travel the same distance
        # dist travelled by p = from p to LCA + LCA to root + from q to LCA
        # dist travelled by q = from q to LCA + LCA to root + from p to LCA
        first = p
        second = q

        while first != second:
            first = first.parent
            if not first:
                first = q

            second = second.parent
            if not second:
                second = p

        return first

    """
    p=5, q=8

            *q
    5   3   8   1   3
    8   1   3   5   3
                *p

    p=5, q=4
            *q
    5   3   4   2   5
    4   2   5   3   5
                    *p
    """
        # go up the tree for both p and q until one of them sees a node that's already visited
        visited = set()

        while p or q:
            if p:
                if p in visited:
                    return p
                visited.add(p)
                p = p.parent
            if q:
                if q in visited:
                    return q
                visited.add(q)
                q = q.parent

