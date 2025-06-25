# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build graph
        adj_lst = defaultdict(set)
        queue = deque()
        queue.append(root)
        visited = set()
        visited.add(root)

        while queue:
            for _ in range(len(queue)):
                pop = queue.popleft()
                if pop.left:
                    adj_lst[pop].add(pop.left)
                    adj_lst[pop.left].add(pop)
                    queue.append(pop.left)
                    visited.add(pop.left)
                if pop.right:
                    adj_lst[pop].add(pop.right)
                    adj_lst[pop.right].add(pop)
                    queue.append(pop.right)
                    visited.add(pop.right)

        # bfs from target node
        visited = set()
        visited.add(target)
        queue.append(target)
        level = 0
        res = []
        while queue and level <= k:
            res = []
            for _ in range(len(queue)):
                pop = queue.popleft()
                res.append(pop.val)
                for nei in adj_lst[pop]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            level += 1

        return res if level > k else []
