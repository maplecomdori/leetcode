class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        seen_odd_freq = False
        for letter, freq in dic.items():
            if freq % 2:
                if seen_odd_freq is False:
                    seen_odd_freq = True
                else:
                    return False
        return True


"""
every character => even frequency
every character => even frequency + one char with odd frequency
"""
