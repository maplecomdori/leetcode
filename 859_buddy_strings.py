class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        lst_idx = []
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
            if s[i] != goal[i]:
                lst_idx.append(i)

        if len(lst_idx) == 0:
            # s = goal
            for n in d.values():
                if n >= 2:
                    # can swap two of the same letters
                    return True
            return False
        elif len(lst_idx) > 2 or len(lst_idx) == 1:
            return False

        lst_s = list(s)
        if lst_idx:
            lst_s[lst_idx[0]], lst_s[lst_idx[1]] = lst_s[lst_idx[1]], lst_s[lst_idx[0]]

        return "".join(lst_s) == goal