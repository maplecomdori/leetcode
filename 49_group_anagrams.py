class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list) # {key: [str]}, where key = 030230 each digit represents a occurence of a char

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # key = "-".join([str(n) for n in count])
            dic[tuple(count)].append(s)

        return dic.values()