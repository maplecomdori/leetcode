class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float("inf")
        t_counter = Counter(t)
        need, have = len(t_counter), 0
        res = ""
        left, right = 0, 0
        counter = defaultdict(int)

        while right < len(s):
            counter[s[right]] += 1
            have = 0
            for c, n in t_counter.items():
                if counter[c] >= n:
                    have += 1
            # print(left, right, s[left:right+1])
            while have == need:
                if have == need:
                    length = right - left + 1
                    if length < min_len:
                        min_len = length
                        res = s[left:right + 1]
                counter[s[left]] -= 1
                if counter[s[left]] < t_counter[s[left]]:
                    have -= 1
                left += 1

            right += 1

        return res


"""
0   1   2   3   4   5   6   7   8   9   10  11  12
A   D   O   B   E   C   O   D   E   B   A   N   C,  ABC
A           B       C               B   A       C
l                   r                               abc
    l               r                               bc
    l                               r               bbc
    l                                   r           abbc
        l                               r           abbc
            l                           r           abbc
                l                       r           abc
                    l                   r           abc
                        l               r           ab
                        l                   r       ab
                        l                       r   abc
                            l                   r   abc
                                l               r   abc
                                    l           r   abc
                                        l       r   ac
                                        l           r

"""