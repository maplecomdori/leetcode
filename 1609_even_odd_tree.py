# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False
        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        level = 1

        while queue:
            # print(level, queue[0].val)
            nxt_level = []
            if level % 2 == 0:
                for i in range(len(queue) - 1):
                    if queue[i].val % 2 == 0:
                        return False
                    if queue[i].val < queue[i + 1].val:
                        if queue[i].left:
                            nxt_level.append(queue[i].left)
                        if queue[i].right:
                            nxt_level.append(queue[i].right)
                    else:
                        return False
                if queue[-1].val % 2 == 0:
                    return False
                if queue[-1].left:
                    nxt_level.append(queue[-1].left)
                if queue[-1].right:
                    nxt_level.append(queue[-1].right)

            else:
                for i in range(len(queue) - 1):
                    if queue[i].val % 2 == 1:
                        return False
                    if queue[i].val > queue[i + 1].val:
                        if queue[i].left:
                            nxt_level.append(queue[i].left)
                        if queue[i].right:
                            nxt_level.append(queue[i].right)
                    else:
                        return False
                if queue[-1].val % 2 == 1:
                    return False
                if queue[-1].left:
                    nxt_level.append(queue[-1].left)
                if queue[-1].right:
                    nxt_level.append(queue[-1].right)

            level += 1
            queue = nxt_level

        return True
