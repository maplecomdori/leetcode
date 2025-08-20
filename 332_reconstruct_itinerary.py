class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()
        adj_lst = {}
        for src, dest in tickets:
            if src not in adj_lst:
                adj_lst[src] = deque()
            adj_lst[src].append(dest)

        res = []

        def dfs(airport):

            while airport in adj_lst and adj_lst[airport]:
                deq = adj_lst[airport]
                nxt = deq.popleft()
                dfs(nxt)
            res.append(airport)

        dfs("JFK")
        return res[::-1]


"""
[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]] => ["JFK","NRT","JFK","KUL"]
JFK: KUL, NRT
NRT: JFK

JFK
    KUL [KUL]
    NRT
        JFK [KUL, JFK]
    [KUL, JFK, NRT]

"""
