class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # find shortest word
        shortest = strs[0]
        for word in strs:
            if len(word) < len(shortest):
                shortest = word

        builder = []
        # check ith character of each jth word match
        for i in range(len(shortest)):
            for j in range(1, len(strs)):
                curr = strs[j]
                prev = strs[j - 1]
                if curr[i] != prev[i]:
                    return "".join(builder)
            builder.append(shortest[i])

        return "".join(builder)