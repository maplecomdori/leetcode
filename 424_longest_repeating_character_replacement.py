class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of character counts
        counter = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in counter:
                counter[s[right]] = 0
            counter[s[right]] += 1

            # remove left most character while the number of characters that are not most frequent char > k
            while True:
                most_frequent_char_count = 0
                most_frequent_char = None
                for char, count in counter.items():
                    if count > most_frequent_char_count:
                        most_frequent_char_count = count
                        most_frequent_char = char
                length = right - left + 1
                if length - most_frequent_char_count > k:
                    left_char = s[left]
                    counter[left_char] -= 1
                    left += 1
                else:
                    break

            max_len = max(max_len, right - left + 1)

        return max_len


"""
A   B   A   B, K=2
l   r           1
l       r
l           r   2

A   B   A   B   C   C   X   X   C, K=2 => 5
l           r

A   B   X   B   B, k=2 => 5

"""