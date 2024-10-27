class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_lst = defaultdict(list)
        in_deg = [0] * numCourses
        res = []

        # build adjency list
        for src, dest in prerequisites:
            adj_lst[src].append(dest)
            in_deg[dest] += 1

        q = deque()

        # add starting nodes with 0 incoming edges
        for node, count in enumerate(in_deg):
            if count == 0:
                q.append(node)

        # run topological sort
        num_visited = 0
        while q:
            pop = q.popleft()
            res.append(pop)
            num_visited += 1

            for nei in adj_lst[pop]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)

        if num_visited == numCourses:
            res.reverse()
            return res
        else:
            return []



        # dfs solution
        res = []

        # build adj_lst
        adj_lst = defaultdict(set)
        for course, preq in prerequisites:
            adj_lst[course].add(preq)

        path = set()
        finished = set()

        def rec(course):
            if course in path:
                return False
            if course in finished:
                return True

            path.add(course)
            for preq in adj_lst[course]:
                if not rec(preq):
                    return False
            path.remove(course)
            finished.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not rec(i):
                return []

        return res