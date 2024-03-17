class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        set_order = set(order)
        s_counter = Counter(s)

        for o_char in order:
            for s_char in s_counter:
                if s_char == o_char:
                    res.append(s_char * s_counter[s_char])

        # append char in s that is not in order
        for s_char in s:
            if s_char not in set_order:
                res.append(s_char)
        return "".join(res)
