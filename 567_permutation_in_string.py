class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = Counter(s1)
        left = 0
        right = 0

        while right < len(s2):
            # print(left, right, counter)
            char = s2[right]
            if char in counter and counter[char] > 0:
                counter[char] -= 1
                if right - left + 1 == len(s1):
                    return True
                right += 1
            else:
                if s2[left] in counter:
                    counter[s2[left]] += 1
                left += 1
        return False
        ########################################################

        if len(s1) > len(s2):
            return False
        # check window size of len(s)
        size = len(s1)
        s1_counter = Counter(s1)
        s2_counter = Counter()

        # create the initial window
        for i in range(size):
            s2_counter[s2[i]] += 1

        for i in range(size, len(s2)):
            if s1_counter == s2_counter:
                return True
            # remove leftmost char in the window
            s2_counter[s2[i - size]] -= 1
            # add a new char at i
            s2_counter[s2[i]] += 1

        return s1_counter == s2_counter


"""
x   x   x   b   a   o   o   o, ab => true

x   x   x   b   o   a   o   o, ab => false

x   x   x   b   b   a   o   o, ab => true
l   l   l   l       r
                l   r

x   x   x   b   a   a   o   o, ab => true

d   b   a   o

b   d   b   a   o


adc, dcda
d   c   d   a
lr
l   r
l       r
    l   r
    l       r
"""