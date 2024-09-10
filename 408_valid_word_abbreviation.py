class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):

            if abbr[j].isdigit():
                # found the start of replacement
                if abbr[j] == '0':
                    # leading 0
                    return False
                # extract the number whose digit can be > 1
                k = j + 1
                while k < len(abbr) and abbr[k].isdigit():
                    k += 1
                number = int(abbr[j:k])

                i += number
                j = k

            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False

        if i == len(word) and j == len(abbr):
            return True


"""
a   p   p   l   e
i   i       i

a   2   e
j   j   j

s55n non-adjacent
s010n leading 0
replacing empty substring


substitution    s10n
substitution    sub4u4
iii    ii   i
substitution    12
i           i

substitution    s55n

"""