class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from one letter and expand left and write (n^2)
        max_len = 0
        res = s[0]
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max_len < right - left + 1:
                    max_len = max(max_len, right - left + 1)
                    res = s[left:right + 1]
                left -= 1
                right += 1

        # start from two letters and expand left and write

        for i in range(len(s) - 1):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max_len < right - left + 1:
                    max_len = max(max_len, right - left + 1)
                    res = s[left:right + 1]
                left -= 1
                right += 1

        return res


"""
b   a   b   a   d
bf => generate all the substring and check if the substring is palindrome (n^3)

b
b   a
b   a   b yes
b   a   b   a
b   a   b   a   d

a
a   b
a   b   a
a   b   a   d



c   b   b   d

"""