class Solution:
    def countAndSay(self, n: int) -> str:

        res = "1"

        for _ in range(n - 1):

            i = 0
            builder = []

            while i < len(res):
                # read consecutive idential number
                end = i + 1
                while end < len(res) and res[i] == res[end]:
                    end += 1
                length = end - i
                builder.append(str(length))
                builder.append(res[i])
                i = end
            res = "".join(builder)

        return res


"""
33  222 5   1
23  32  15  11


"""