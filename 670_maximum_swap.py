class Solution:
    def maximumSwap(self, num: int) -> int:
        # starting from the end, keep the max seen so far in an array

        lst = deque()  # monotonic (max_val, max_val_idx)
        string_lst = list(str(num))
        for i in range(len(string_lst) - 1, -1, -1):
            char = string_lst[i]
            if not lst:
                lst.appendleft((char, i))
                continue

            if char > lst[0][0]:
                lst.appendleft((char, i))
            else:
                lst.appendleft(lst[0])

        # starting from the left, find the first number less than max seen so far at that position

        for i in range(len(string_lst)):
            char = string_lst[i]
            max_from_right = lst[i][0]
            max_from_right_idx = lst[i][1]
            if char < max_from_right:
                string_lst[i], string_lst[max_from_right_idx] = string_lst[max_from_right_idx], string_lst[i]
                break

        return int("".join(string_lst))

####################################################################
        # brute force o(n^2)
        string = str(num)

        for i, char in enumerate(string):
            curr = int(char)
            max_val = curr
            max_idx = i
            # find the index of the max digit to the right of string[i], if multiple max_val, use the last one
            for j in range(i + 1, len(string)):
                val = int(string[j])
                if val >= max_val:
                    max_idx = j
                    max_val = val
            if max_val > curr:
                lst_string = list(string)
                lst_string[i], lst_string[max_idx] = lst_string[max_idx], lst_string[i]
                return int("".join(lst_string))

        return num
"""
2   7   3   6
    =
    =       =
    =       =
    =       =
    =   =   =
=   =   =   =
=   =   =   =
switch the largest digit with a smaller digit that comes before the largest digit

2   2   1   1
=   =
=   =   =   =


1   0   => cannot switch with 0 

2   7   3   8   => 8732
            =
    =       =
    =       =
    =       =
    =       =
    =   =   =
=   =   =   =
=   =   =   =


4   2   7   3   8   => 8732
                =
        =       =
        =       =
        =       =
        =       =
        =   =   =
    =   =   =   =
    =   =   =   =

1   9   9   3 => 9931 not 9193, use the last max_val if there are 2 9s (max_vals)
"""