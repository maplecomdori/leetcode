class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []  # index of opening bracket
        include = [False] * len(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            elif s[i] == ")":
                if stack:
                    # add ")" only if there is a corresponding closing bracket
                    idx = stack.pop()
                    include[idx] = True
                    include[i] = True
            else:
                include[i] = True

        return "".join([s[i] for i in range(len(s)) if include[i]])
