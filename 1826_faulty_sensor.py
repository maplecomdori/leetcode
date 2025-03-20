class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        i, j = 0, 0
        # find the first index that has different values in sensor1 and sensor2
        while i < len(sensor1) and j < len(sensor2) and sensor1[i] == sensor2[j]:
            i += 1
            j += 1

        if i == len(sensor1) and j == len(sensor2) or i + 1 == len(sensor1) and j + 1 == len(sensor2):
            return -1

        # try advancing i
        x = i + 1
        y = j
        while x < len(sensor1) and sensor1[x] == sensor2[y]:
            x += 1
            y += 1

        # try advancing j
        a = i
        b = j + 1
        while b < len(sensor2) and sensor1[a] == sensor2[b]:
            a += 1
            b += 1

        if x == len(sensor1) and b == len(sensor2):
            return -1

        if x == len(sensor1):
            return 2

        if b == len(sensor2):
            return 1

        return -1


"""
2   3   4   5
i
    i
        i
2   1   3   4
j
    j   j
            j
2 choices -> advance i or j
second one runs out first => correct
================================================
2   2   2   2   2
i   i   i   i   i
2   2   2   2   5
j   j   j   j   j

advancing i or j => out of bounds

================================================
2   3   2   2   3   2
i   i   i   i
                i
                    i
2   3   2   3   2   7
j   j   j   j
            j
                j


2   3   2   2   3   2
i   i   i   i
            i
                i

2   3   2   3   2   7
j   j   j   j
                j
                    j => different again => can't reach the end
"""