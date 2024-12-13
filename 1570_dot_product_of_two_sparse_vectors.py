class SparseVector:
    def __init__(self, nums: List[int]):
        # save only non-zero values with index
        self.nonzeros = []
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros.append([i, n])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # go through each pair (index, value) in each vector
        # multiply only when two indices match
        # if no match, advance the smaller index
        i = 0
        j = 0
        total = 0
        while i < len(self.nonzeros) and j < len(vec.nonzeros):
            if self.nonzeros[i][0] == vec.nonzeros[j][0]:
                total += self.nonzeros[i][1] * vec.nonzeros[j][1]
                i += 1
                j += 1
            elif self.nonzeros[i][0] < vec.nonzeros[j][0]:
                i += 1
            else:
                j += 1
        return total


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)