class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # concatenation solution
        if len(s) != len(goal):
            return False

        return goal in s + s

        # brute force
        if len(s) != len(goal):
            return False

        def compare_from(i):
            # compare 's' starting at i and 'goal' starting from 0
            j = 0
            while j < len(goal):
                if s[i] != goal[j]:
                    return False
                i = (i + 1) % len(goal)
                j += 1
            return True

        for i in range(len(s)):
            if s[i] == goal[0] and compare_from(i):
                return True

        return False


"""
aabcde  abcdea
"""