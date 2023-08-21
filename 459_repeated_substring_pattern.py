class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for r in range(len(s) // 2):
            # check if you can repeat the substring s[:r+1] for the rest of the string
            ss = s[:r+1]
            start = r + 1

            b = True
            while b and start <= len(s):
                if start == len(s):
                    return True
                for i in range(len(ss)):
                    if start + i >= len(s) or ss[i] != s[start + i]:
                        b = False
                        break
                start += len(ss)

        return False
