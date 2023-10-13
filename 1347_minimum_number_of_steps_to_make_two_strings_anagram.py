class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # count characters
        s_counter = Counter(s)
        t_counter = Counter(t)

        # count only when a character appears more in s than t
        total = 0
        for c, n in s_counter.items():
            if c not in t_counter:
                total += n
            else:
                if n > t_counter[c]:
                    total += n - t_counter[c]

        return total


"""
b   a   b
a   b   a

a
b

a   a
a   b

b   a   b
a   b   b

a   b   b   c   c   c   d   d   d   d
a   a   b   c   c   d   d   d   d   d
    *               *

l   e   e   t   c   o   d   e
p   r   a   c   t   i   c   e

l: 1
e: 2
t: 0
c: -1
o: 1
d: 1


"""