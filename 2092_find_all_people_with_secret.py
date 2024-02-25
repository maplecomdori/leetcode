class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # build adj_lst
        adj_lst = defaultdict(list) # {src: [dst, time]}
        for src, dst, time in meetings:
            adj_lst[src].append((dst, time))
            adj_lst[dst].append((src, time))

        in_the_know = set([0, firstPerson])
        start = 0

        def dfs(node, time):
            if node in in_the_know:
                return
            in_the_know.add(node)
            for nei, t in adj_lst[node]:
                if t == time:
                    dfs(nei, time)

        while start < len(meetings):
            time = meetings[start][2]
            end = start + 1

            # find the meetings happening at the same time
            while end < len(meetings) and meetings[end][2] == time:
                end += 1

            # do dfs / bfs at each time,
            # for each path that includes one of the people with the secret, add everyone in the path to the know set

            for i in range(start, end):
                src = meetings[i][0]
                dst = meetings[i][1]
                curr_time = meetings[i][2]

                if src in in_the_know or dst in in_the_know:
                    dfs(src, curr_time)
                    dfs(dst, curr_time)

            start = end

        return in_the_know