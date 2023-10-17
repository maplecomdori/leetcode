class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        # build adj_lst
        adj_lst = defaultdict(list)
        parent = [-1] * n

        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            if left != -1:
                adj_lst[i].append(left)
                parent[left] = i
            if right != -1:
                adj_lst[i].append(right)
                parent[right] = i

        # find the root
        root = None
        for i in range(n):
            if adj_lst[i] and parent[i] == -1:
                root = i
                break

        # run BFS
        q = deque([root])
        visited = set([root])

        while q:
            for _ in range(len(q)):
                pop = q.popleft()

                for child in adj_lst[pop]:
                    if child in visited:
                        return False
                    visited.add(child)
                    q.append(child)

        return len(visited) == n