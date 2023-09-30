class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        n_out_of_place = 0
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            if c1 == c2:
                continue
            else:
                counter1[c1] += 1
                counter2[c2] += 1
                n_out_of_place += 1

        if n_out_of_place > 2 or counter1 != counter2:
            return False

        return True
"""
b   a   n   k
k   a   n   b
exactly two chars can be out of place
all character count should match

"""