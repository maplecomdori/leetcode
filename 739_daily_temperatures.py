class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)

        return answer

"""
73  74  75  71  69  72  76  73
[(73,0)] []
[(74,1]] [1 0 0 0 0 0 0 0]
[(75,2)] [1 1 0 0 0 0 0 0]
[(75,2) (71,3)] [1 1 0 0 0 0 0 0]
[(75,2) (71,3) (69,4)] [1 1 0 0 0 0 0 0]
[(75,2) (72,5)] [1 1 0 2 1 0 0 0]
[(76,6)] [1 1 4 2 1 1 0 0]
[(76,6) (73,7)] [1 1 4 2 1 1 0 0]
"""