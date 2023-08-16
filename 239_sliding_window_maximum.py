class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        deq = deque()  # (index, number)
        # keep the larget 'number' at the front => deq in a decreasing order

        # process first window
        for i in range(k):
            while deq and deq[-1][1] < nums[i]:
                deq.pop()
            deq.append((i, nums[i]))
        res = [deq[0][1]]

        # process the rest of the remaining sliding windows
        left = 1
        right = k

        while right < len(nums):
            while deq and deq[-1][1] < nums[right]:
                # remove elements < the rightmost element
                deq.pop()
            deq.append((right, nums[right]))
            if deq and deq[0][0] < left:
                # kick out the most left element
                deq.popleft()

            res.append(deq[0][1])

            left += 1
            right += 1

        return res