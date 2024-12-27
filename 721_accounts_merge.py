class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # build graph
        adj_lst = {}  # {email: [nei emails]}
        dic = {}  # {email: name}

        for act in accounts:
            # print(act)
            name = act[0]
            src_email = act[1]

            if src_email not in adj_lst:
                adj_lst[src_email] = set()
            dic[src_email] = name

            idx = 2
            while idx < len(act):
                dest_email = act[idx]
                if src_email not in adj_lst:
                    adj_lst[src_email] = set()
                adj_lst[src_email].add(dest_email)
                if dest_email not in adj_lst:
                    adj_lst[dest_email] = set()
                adj_lst[dest_email].add(src_email)

                dic[dest_email] = name
                idx += 1
        # print(adj_lst)

        # build solution
        res = []
        visited = set()
        for email in adj_lst:
            if email in visited:
                continue
            email_lst = []
            queue = deque()
            queue.append(email)
            visited.add(email)

            while queue:
                for _ in range(len(queue)):
                    pop = queue.popleft()
                    email_lst.append(pop)

                    for nei in adj_lst[pop]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            email_lst.sort()
            # print(email, email_lst)
            res.append([dic[email]] + email_lst)

        res.sort(key=lambda x: x[0])

        return res


"""
common email => same account (name)
[ [ name, emails in sorted order ] ]

"""