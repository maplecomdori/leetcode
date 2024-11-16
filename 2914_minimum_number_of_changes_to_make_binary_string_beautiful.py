class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        count = 0

        while i < len(s):
            if s[i] != s[i+1]:
                count += 1
            i += 2
        return count


"""
given even length
beautiful
    - substring length is even
    - only 1 or 0


00 => 0
10 => 1
11 => 0

0000
0001
0011
0101
101

"""