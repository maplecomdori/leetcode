class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_idx = {}  # remember the last index the char appeared
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            if char in char_to_idx and char_to_idx[char] >= left:
                # 'abba' would fail without the second condition
                left = 1 + char_to_idx[char]
            max_len = max(max_len, right - left + 1)
            char_to_idx[char] = right

        return max_len
        ########################################################
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
        ########################################################
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