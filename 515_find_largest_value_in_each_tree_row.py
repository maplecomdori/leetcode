class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        q = deque([root])

        while q:
            max_val = float("-inf")
            for _ in range(len(q)):
                pop = q.popleft()
                max_val = max(max_val, pop.val)

                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            res.append(max_val)

        return res