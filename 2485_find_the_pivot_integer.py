class Solution:
    def pivotInteger(self, n: int) -> int:
        forward = []
        backward = []

        total = 0
        for i in range(1, n + 1):
            total += i
            forward.append(total)

        total = 0

        for i in range(n, 0, -1):
            total += i
            backward.append(total)

        backward.reverse()
        for i in range(len(forward)):
            if forward[i] == backward[i]:
                return i + 1

        return -1
