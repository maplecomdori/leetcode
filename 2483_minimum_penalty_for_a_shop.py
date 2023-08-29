class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # shop open + no customer => 1
        # shop closed + customer => 1
        cur_penalty = sum([1 if c == "Y" else 0 for c in customers])
        min_val = cur_penalty
        d = {}  # {penalty: index}

        for i in range(len(customers)):
            # close at ith hour and update the penalty at i (lst_penalty)
            if customers[i] == "N":
                cur_penalty += 1
            elif customers[i] == "Y":
                cur_penalty -= 1

            # update min_val and its index
            if cur_penalty < min_val:
                min_val = cur_penalty
                if min_val not in d:
                    # save the first index where the current minimum penalty was found
                    d[min_val] = i + 1

        return d[min_val] if min_val in d else 0