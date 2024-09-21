class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        i, j, k = 0, 0, 0

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            max_val = max(arr1[i], arr2[j], arr3[k])
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] < max_val:
                    i += 1
                if arr2[j] < max_val:
                    j += 1
                if arr3[k] < max_val:
                    k += 1

        return res