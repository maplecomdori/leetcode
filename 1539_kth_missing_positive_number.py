class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1

        for num in arr:
            if num == curr:
                curr += 1
            else:
                missing = num - curr
                if missing >= k:
                    break
                k -= missing
                curr = num + 1

        return curr + k - 1
