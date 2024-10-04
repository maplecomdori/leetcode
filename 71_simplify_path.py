class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        left = 0
        right = 0

        while right < len(path):
            # skip slash
            if path[right] == '/':
                right += 1
                left = right
                continue

            # parse . or .. or name
            while right < len(path) and path[right] != '/':
                right += 1

            string = path[left:right]
            left = right

            # if .
            if string == '.':
                pass

            # elif ..
            elif string == '..':
                stack.pop() if stack else None
            # else filename
            else:
                stack.append(string)

        # add / at the beg
        return '/' + "/".join(stack)


"""
.   => curr directory
..  => parent
///  => /

not match the above => directory or file name

simpliefied canonical path
- start with /
- one slash separator
- not end with / except root
- not have . and .. used to denote current or parent directories


"""