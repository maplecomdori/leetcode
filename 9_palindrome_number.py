class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # get the lagest n in 10^n to get the first digit
        divisor = 1
        while x >= 10 * divisor:
            divisor *= 10

        while x:
            head = x // divisor
            tail = x % 10
            if head != tail:
                return False
            # remove head
            x %= divisor
            # remove tail
            x //= 10
            divisor //= 100

        return True


"""
121

100

1000021

"""