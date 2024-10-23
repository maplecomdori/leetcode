class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        visited = set()

        def rec(a, b):
            if a + b == target:
                return True
            if (a, b) in visited:
                return False

            visited.add((a, b))
            # fill a/b to the top
            top_a = rec(x, b)
            top_b = rec(a, y)

            # empty a/b
            empty_a = rec(0, b)
            empty_b = rec(a, 0)

            # transfer a to b
            b_room = y - b
            if a <= b_room:
                transfer_a = rec(0, b + a)
            else:
                transfer_a = rec(a - b_room, y)

            # transfer b to a
            a_room = x - a
            if b <= a_room:
                transfer_b = rec(a + b, 0)
            else:
                transfer_b = rec(x, b - a_room)

            return top_a or top_b or empty_a or empty_b or transfer_a or transfer_b

        return rec(0, 0)
