class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycle in the graph

        # build adj_lst
        adj_lst = {}  # {course: [prerequisite]}

        for crs, pre in prerequisites:
            if crs not in adj_lst:
                adj_lst[crs] = [pre]
            else:
                adj_lst[crs].append(pre)

        # traverse graph
        visited = set()
        can_finish = set()

        def rec(node):
            if node in can_finish:
                return True
            if node not in adj_lst:
                return True
            if node in visited:
                return False
            visited.add(node)
            for nei in adj_lst[node]:
                if not rec(nei):
                    return False
            visited.remove(node)
            can_finish.add(node)
            return True

        for i in range(numCourses):
            if not rec(i):
                return False
        return True


"""
[a, b] => take b first, then a



"""