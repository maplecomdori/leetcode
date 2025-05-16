# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        node = self.stack[-1]

        # push all the left to the stack
        while self.stack and node.left:
            self.stack.append(node.left)
            node = node.left

    def next(self) -> int:
        elem = self.stack.pop()

        # add the right child and all of its left node to the stack
        node = elem.right

        while node:
            self.stack.append(node)
            node = node.left

        return elem.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()