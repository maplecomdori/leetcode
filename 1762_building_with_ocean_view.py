class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_height = -1
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                ans.append(i)
                max_height = heights[i]
        ans.reverse()
        return ans

        # stack solution
        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            stack.append(i)

        return stack


"""
4   2   3   1   ocean
=
=       =
=   =   =   
=   =   =   =   ocean


"""