class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        builder = []
        for string in strs:
            builder.append(f"{len(string)}#{string}")
        return "".join(builder)
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):
            # read length
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length

        return res

"""
Hello,World
5#Hello5#World

1#Hello,World
7#1#Hello,5#World

"0"
1#0

"""