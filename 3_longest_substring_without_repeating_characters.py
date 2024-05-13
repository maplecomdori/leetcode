class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            max_len = max(max_len, r - l + 1)

        return max_len
        ##############################
        d = {}  # {c: last_index}
        l = 0
        max_len = 0
        for i, c in enumerate(s):
            if c not in d:
                max_len = max(max_len, i - l + 1)
                d[c] = i
            else:
                new_l = d[c] + 1
                for j in range(l, new_l):
                    del d[s[j]]
                l = new_l
                d[c] = i

        return max_len
"""
a   b   c   a   b   c   b   b => remember the last occurence of each char in dic

p   w   w   k   e   w
lr
l       r
        lr
        l   r
        l       r
        l           r
            l       r

a   b   c   d   b   a   z
"""