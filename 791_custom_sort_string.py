class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []

        # append characters of 's' that appear in 'order'
        for c in order:
            if c in counter:
                res.append(c * counter[c])
            del counter[c]

        # append unused letter
        for c in counter:
            res.append(c * counter[c])

        return "".join(res)


"""
order   s       result
cba     abcd    cbad

bcafg   abcd    bcafg

cba     abcxxx   cbaxxx

cbazzz  abcd    cbad
"""