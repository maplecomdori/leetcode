class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        last_end = 0

        for log in logs:
            fid, action, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if not stack:
                stack.append((fid, action, time))
                continue

            last_id = stack[-1][0]

            if action == 'start':
                duration = time - last_end
                res[last_id] += duration
                last_end = time
                stack.append((fid, action, time))

            elif action == 'end':
                duration = time + 1 - last_end
                res[last_id] += duration
                last_end = time + 1
                stack.pop()

        return res
"""
EXAMPLE 2
0   1   2   3   4   5   6   7   8   9   10
A(
        A(
                    A)
                        A(
                        A)
                            A)

EXAMPLE 3
0   1   2   3   4   5   6   7   8   9   10
A(
        A(
                    A)
                        B(
                        B)
                            A)

EXAMPLE 4
0   1   2   3   4   5   6   7   8   9   10
A(
        A(
                    A)
                            B(
                            B)
                                A)
                        AAAA
"""