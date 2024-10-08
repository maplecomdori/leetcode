class Solution:
    def validPalindrome(self, s: str) -> bool:

        # try deleting one from right
        has_chance = True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif has_chance:
                right -= 1
                has_chance = False
            else:
                break

        if left >= right:
            return True

        # try deleting one from left
        has_chance = True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif has_chance:
                left += 1
                has_chance = False
            else:
                break

        if left >= right:
            return True

        return False


"""
abbca
acbba
"""