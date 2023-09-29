class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        lst = list(zip(profit, difficulty))

        # sort by profit first and difficulty
        # if two jobs with different difficulty, more difficult one comes first
        lst.sort(reverse=True)
        worker.sort(reverse=True)

        profit_ptr = 0
        worker_ptr = 0
        total = 0

        # assign workers to the most profitable job first
        while worker_ptr < len(worker) and profit_ptr < len(lst):
            while profit_ptr < len(lst) and worker[worker_ptr] < lst[profit_ptr][1]:
                profit_ptr += 1
            if profit_ptr >= len(lst):
                return total
            total += lst[profit_ptr][0]
            worker_ptr += 1
        return total
