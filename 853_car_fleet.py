class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst_pairs = list(zip(position, speed))
        lst_pairs.sort(key=lambda x: x[0], reverse=True)
        # print(lst_pairs)
        arrival_times = [(target - pos) / sp for pos, sp in lst_pairs]
        # print(arrival_times)

        stack = []
        for time in arrival_times:
            slowest = time
            if stack and stack[-1] >= slowest:
                pop = stack.pop()
                slowest = pop
            stack.append(slowest)

        return len(stack)
"""
1   1   7   3   12
[1]
[1 1] pop [1]
[1 7]
[1 7] pop [1 7]
[1 7 12]

"""