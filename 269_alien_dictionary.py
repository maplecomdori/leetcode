class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build adj_lst
        adj_lst = defaultdict(set)

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            min_len = min(len(first), len(second))
            if first[:min_len] == second[:min_len]:
                if len(first) > len(second):
                    return ""
                else:
                    continue
            # find the first different character
            for k in range(min_len):
                if first[k] != second[k]:
                    adj_lst[first[k]].add(second[k])
                    break

        # count in degree for all vertices
        in_deg = {u: 0 for w in words for u in w}
        for s in adj_lst.values():
            for u in s:
                in_deg[u] += 1

        q = deque()
        for c in in_deg:
            if in_deg[c] == 0:
                q.append(c)

                # topological sort

        res = []
        while q:
            for _ in range(len(q)):
                pop = q.popleft()
                res.append(pop)
                for nei in adj_lst[pop]:
                    in_deg[nei] -= 1
                    if in_deg[nei] == 0:
                        q.append(nei)

        if len(res) < len(in_deg):
            # not all letters processed
            return ""
        return "".join(res)
