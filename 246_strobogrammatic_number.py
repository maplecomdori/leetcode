class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        inverse = {'1': '1', '6': '9', '9': '6', '0': '0', '8': '8'}

        # compare from start with end
        start = 0
        end = len(num) - 1

        while start <= end:
            start_char = num[start]
            end_char = num[end]

            if start_char not in inverse or inverse[start_char] != end_char:
                return False
            start += 1
            end -= 1

        return True


"""
69 => true
88 => true
1 => true
11 => true
619 => true
96 => true
25 => false
0 => true
00 => invalid input
6699
6009
639 => false, process the middle digit
"""
