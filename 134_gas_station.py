class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O(n) solution
        diff = []
        total = 0
        for g, c in zip(gas, cost):
            tmp = g - c
            diff.append(tmp)
            total += tmp
        if total < 0:
            return -1

        total = 0
        start = 0
        for i in range(len(diff)):
            total += diff[i]

            if total < 0:
                start = i + 1
                total = 0

        return start

        # n^2 solution
        # try starting at each index
        for start in range(len(gas)):
            # try if you can complete a run
            tank = 0
            idx = start
            while True:
                tank += gas[idx] - cost[idx]
                if tank < 0:
                    break
                idx += 1
                idx %= len(gas)
                if idx == start:
                    return start

        return -1


"""
1   2   3   4   5
3   4   5   1   2

0+1-3 < 0 => not possible
0+2-4 < 0 => not possible
0+3-5 < 0 => not possible
0+4-1 = 3 => can go to next station
3+5-2 = 6 => can go to next station
6+1-3 = 4 => can go to next station
4+2-4 = 2 => can go to next station
2+3-5 = 0 => can go to next station
return

2   3   4
3   4   3

0+2-3 < 0
0+3-4 < 0
0+4-3=1 => nxt
1+2-3=0 => nxt
0+3-4 < 0
"""