class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_char = set(allowed)
        count = 0
        for word in words:
            skip = False
            for char in word:
                if char not in set_char:
                    skip = True
                    break
            if skip:
                continue
            else:
                count += 1

        return count