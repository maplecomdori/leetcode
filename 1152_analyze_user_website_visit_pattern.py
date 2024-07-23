class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # user: [website visited in order] == [(timestamp, website)]
        history = defaultdict(list)

        for u, t, w in zip(username, timestamp, website):
            history[u].append((t, w))

        for u, lst in history.items():
            lst.sort()

        # find all the possible patterns for each user and count
        counter = defaultdict(int)
        for u, lst in history.items():
            path = []
            visited = set()
            for i in range(len(lst) - 2):
                path.append(lst[i][1])
                for j in range(i + 1, len(lst) - 1):
                    path.append(lst[j][1])
                    for k in range(j + 1, len(lst)):
                        path.append(lst[k][1])
                        key = "-".join(path)
                        path.pop()
                        if key in visited:
                            continue
                        visited.add(key)
                        counter[key] += 1
                    path.pop()
                path.pop()

        max_val = 0
        max_key = None
        for k, v in counter.items():
            key = k.split("-")
            if v > max_val or (v == max_val and key < max_key):
                max_val = v
                max_key = key

        return max_key

