class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        disallowed = set(deadends)
        if '0000' in deadends:
            return -1
        queue = deque(['0000'])
        moves = 0

        def increment(str_digit):
            int_val = (int(str_digit) + 1) % 10
            return str(int_val)
        def decrement(str_digit):
            int_val = int(str_digit) - 1
            if int_val < 0:
                int_val = 9
            return str(int_val)

        while queue:
            for _ in range(len(queue)):
                pop = queue.popleft()
                if pop == target:
                    return moves
                for idx in range(4):
                    inc_lst = list(pop)
                    inc_lst[idx] = increment(inc_lst[idx])
                    inc_string = "".join(inc_lst)
                    if inc_string not in disallowed:
                        queue.append(inc_string)
                        disallowed.add(inc_string)
                    dec_lst = list(pop)
                    dec_lst[idx] = decrement(dec_lst[idx])
                    dec_string = "".join(dec_lst)
                    if dec_string not in disallowed:
                        queue.append(dec_string)
                        disallowed.add(dec_string)
            moves += 1
        return -1

"""
4 wheels
9 => 0
0 => 9

0101    0102    0201    1212    2002, target=0202

"""