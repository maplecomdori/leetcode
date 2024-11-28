class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dct = defaultdict(list)  # {key: [one group]}

        for string in strings:
            if len(string) == 1:
                dct[(0)].append(string)
                continue

            builder = []
            for i in range(1, len(string)):
                first = string[i - 1]
                second = string[i]
                if first <= second:
                    builder.append(ord(second) - ord(first))
                else:
                    builder.append(ord(second) - ord(first) + 26)
            dct[tuple(builder)].append(string)

        return list(dct.values())


"""
az    ba
25-0  1-2=-1

xyz yza
"""