class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])

        # find the row using binary search
        top, bottom = 0, N - 1
        row = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            first = matrix[mid][0]
            last = matrix[mid][-1]

            if target < first:
                bottom = mid - 1
            elif last < target:
                top = mid + 1
            else:
                row = mid
                break
        if row < 0:
            return False

        # find if the target exists in the row
        left, right = 0, M - 1

        while left <= right:
            mid = (left + right) // 2
            elem = matrix[row][mid]
            if elem == target:
                return True
            elif elem < target:
                left = mid + 1
            else:
                right = mid - 1

        return False