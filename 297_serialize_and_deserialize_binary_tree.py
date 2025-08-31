# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        # preorder traversal
        builder = []

        def rec(node):
            if not node:
                builder.append('null')
                return

            builder.append(str(node.val))
            rec(node.left)
            rec(node.right)

        rec(root)
        return ",".join(builder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        lst = data.split(',')
        idx = 0

        def rec():
            nonlocal idx
            if lst[idx] == 'null':
                idx += 1
                return None

            node = TreeNode(int(lst[idx]))
            idx += 1
            node.left = rec()
            node.right = rec()

            return node

        return rec()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))